# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from __future__ import print_function

import roslib
roslib.load_manifest('camera_pkg')
import cv2
import numpy as np
from face_detector import get_face_detector, find_faces
from face_landmarks import get_landmark_model, detect_marks
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import dlib
from mtcnn import MTCNN
import numpy as np
import os
import tensorflow as tf
from tensorflow import keras

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

class imageConverter:

    # publishes modified/processed images
    def __init__(self):
        self.correctPos = bool == False
        self.correctPlac = bool == False
        self.image_pub = rospy.Publisher("/camera/rgb/image_processed", Image, queue_size=1)
        self.bridge = CvBridge()
        # subscribes to rgb/image_raw topic
        self.image_sub = rospy.Subscriber("/camera/rgb/image_raw", Image, self.callback, queue_size=1)
        self.detector2 = dlib.get_frontal_face_detector()
        self.modelFile = "models/res10_300x300_ssd_iter_140000.caffemodel"
        self.configFile = "models/deploy.prototxt.txt"
        self.net = cv2.dnn.readNetFromCaffe(self.configFile, self.modelFile)
        self.classifier2 = cv2.CascadeClassifier('models/haarcascade_frontalface2.xml')

    # callback function to convert image to opencv format
    def callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as e:
            print(e)
            return

        # show image output in 'image raw' window
        cv2.imshow("Image raw", cv_image)
        cv2.waitKey(3)

        # draw shape on the image
        (rows, cols, channels) = cv_image.shape

        font = cv2.FONT_HERSHEY_SIMPLEX
        img2 = cv2.resize(cv_image, None, fx=0.5, fy=0.5)
        height, width = img2.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(img2, (300, 300)),
                                     1.0, (300, 300), (104.0, 117.0, 123.0))

        self.net.setInput(blob)
        faces3 = self.net.forward()
        faces4 = self.classifier2.detectMultiScale(img2)

        for i in range(faces3.shape[2]):
            confidence = faces3[0, 0, i, 2]
            if confidence > 0.5:
                box = faces3[0, 0, i, 3:7] * np.array([width, height, width, height])
                (x, y, x1, y1) = box.astype("int")
                cv2.rectangle(img2, (120, 85), (208, 192), 1)
                cv2.rectangle(img2, (120, 120), (208, 140), 3)
                cv2.rectangle(img2, (x, y), (x1, y1), (0, 0, 255), 2)
                if (120<x<150) and (85<y<115) and (177<x1<208) and (162<y1<192):
                    self.correctPlac = True
                else:
                    self.correctPlac = False

        def eye_on_mask(mask, side, shape):
            points = [shape[i] for i in side]
            points = np.array(points, dtype=np.int32)
            mask = cv2.fillConvexPoly(mask, points, 255)
            l = points[0][0]
            t = (points[1][1] + points[2][1]) // 2
            r = points[3][0]
            b = (points[4][1] + points[5][1]) // 2
            return mask, [l, t, r, b]

        def find_eyeball_position(end_points, cx, cy):
            x_ratio = (end_points[0] - cx) / (cx - end_points[2])
            y_ratio = (cy - end_points[1]) / (end_points[3] - cy)
            if x_ratio > 3:
                return 1
            elif x_ratio < 0.33:
                return 2
            elif y_ratio < 0.33:
                return 3
            else:
                return 0

        def contouring(thresh, mid, img2, end_points, right=False):

            cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            try:
                cnt = max(cnts, key=cv2.contourArea)
                M = cv2.moments(cnt)
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                if right:
                    cx += mid
                cv2.circle(img2, (cx, cy), 4, (0, 0, 255), 2)
                pos = find_eyeball_position(end_points, cx, cy)
                if 120<cy<140:
                    self.correctPos = True
                else:
                    self.correctPos = False
                if (self.correctPos == True) and (self.correctPlac == True):
                    cv2.putText(img2, 'Correct Position!', (30, 30), font, 1, (255, 255, 0), 2, cv2.LINE_AA)
                return pos
            except:
                pass

        def process_thresh(thresh):
            thresh = cv2.erode(thresh, None, iterations=2)
            thresh = cv2.dilate(thresh, None, iterations=4)
            thresh = cv2.medianBlur(thresh, 3)
            thresh = cv2.bitwise_not(thresh)
            return thresh

        #def print_eye_pos(img2, left, right):
            #if left == right and left != 0:
                #text = ''
                #if left == 1:
                    #print('Looking left')
                    #text = 'Looking left'
                #elif left == 2:
                 #   print('Looking right')
                  #  text = 'Looking right'
                #elif left == 3:
                #    print('Looking up')
                #    text = 'Looking up'
                #font = cv2.FONT_HERSHEY_SIMPLEX
                #cv2.putText(img2, text, (30, 30), font,
                #            1, (0, 255, 255), 2, cv2.LINE_AA)

        face_model = get_face_detector()
        landmark_model = get_landmark_model()
        left = [36, 37, 38, 39, 40, 41]
        right = [42, 43, 44, 45, 46, 47]

        thresh = img2.copy()

        cv2.namedWindow('image')
        kernel = np.ones((9, 9), np.uint8)

        def nothing(x):
            pass

        cv2.createTrackbar('threshold', 'image', 75, 255, nothing)

        rects = find_faces(img2, face_model)

        for rect in rects:
            shape = detect_marks(img2, landmark_model, rect)
            mask = np.zeros(img2.shape[:2], dtype=np.uint8)
            mask, end_points_left = eye_on_mask(mask, left, shape)
            mask, end_points_right = eye_on_mask(mask, right, shape)
            mask = cv2.dilate(mask, kernel, 5)
            eyes = cv2.bitwise_and(img2, img2, mask=mask)
            mask = (eyes == [0, 0, 0]).all(axis=2)
            eyes[mask] = [255, 255, 255]
            mid = int((shape[42][0] + shape[39][0]) // 2)
            eyes_gray = cv2.cvtColor(eyes, cv2.COLOR_BGR2GRAY)
            threshold = cv2.getTrackbarPos('threshold', 'image')
            _, thresh = cv2.threshold(eyes_gray, threshold, 255, cv2.THRESH_BINARY)
            thresh = process_thresh(thresh)

            eyeball_pos_left = contouring(thresh[:, 0:mid], mid, img2, end_points_left)
            eyeball_pos_right = contouring(thresh[:, mid:], mid, img2, end_points_right, True)
            print_eye_pos(img2, eyeball_pos_left, eyeball_pos_right)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cv2.imshow("dnn", img2)

        try:
            self.image_pub.publish(self.bridge.cv2_to_imgmsg(img2, "bgr8"))
        except CvBridgeError as e:
            print(e)



# main function to run the code
def main(args):
    ic = imageConverter()
    rospy.init_node('imageConverter', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main(sys.argv)

