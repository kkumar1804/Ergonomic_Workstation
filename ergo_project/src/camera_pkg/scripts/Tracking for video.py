#!/usr/bin/env python3

from __future__ import print_function

import roslib
roslib.load_manifest('camera_pkg')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:

  #publishes modified/processed images
  def __init__(self):
    self.image_pub = rospy.Publisher("/camera/rgb/image_processed",Image, queue_size= 1)

    self.bridge = CvBridge()
    #subscribes to rgb/image_raw topic
    self.image_sub = rospy.Subscriber("/camera/rgb/image_raw",Image,self.callback, queue_size= 1)

  #callback function to convert image to opencv format
  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

    #show image output in 'image raw' window
    cv2.imshow("Image raw", cv_image)
    cv2.waitKey(3)
 
    #draw shape on the image
    (rows,cols,channels) = cv_image.shape
    if cols > 60 and rows > 60 :
      cv2.circle(cv_image, (350,250), 100, 500)
      cv2.line(cv_image, (250,260), (450,260), 1)
    
    #show processed image in 'image window' window
    cv2.imshow("Image window", cv_image)
    cv2.waitKey(3)

    try:
      self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))
    except CvBridgeError as e:
      print(e)

#main function to run the code
def main(args):
  ic = image_converter()
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
