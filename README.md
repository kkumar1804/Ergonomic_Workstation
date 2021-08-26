# Ergonomic Workstation Project

The aim of this project is to help people who are struggling with back and neck pains due to sub-optimal posture when working. The camera (placed on top of the monitor) scans the user and verifies if they are in the correct posture or not (i.e eyes in line with the top of the monitor and looking straight at the screen). There is potential for this project to be developed further to aid people in correcting their posture when working.

**Requirements:**
- Ros Noetic install
- Orbbec Astra Pro camera 

**Installing packages:**

- Ros Noetic:
  
  ```
  sudo apt install ros-noetic-desktop-full
  ```
- Open CV:

  Using pip:
  ```
  pip install opencv-python
  ```
  Using Anaconda:
  ```
  conda install -c conda-forge opencv
  ```
- Dlib:

  Using pip:
  ```
  pip install dlib
  ```
  Using Anaconda:
  ```
  conda install -c menpo dlib
  ```
- Tensorflow:
  
  Using pip:
  ```
  pip install tensorflow
  ```
  
  Using Anaconda:
  ```
  conda install -c conda-forge tensorflow
  ```

**Using the Astra Camera:**

You will need to clone this github repo: https://github.com/orbbec/ros_astra_camera

You will also need to clone this repo to your workspace: https://github.com/vardanagarwal/Proctoring-AI

Once the 'Proctoring AI' and the 'ros astra camera' repositories are cloned, the files 'RGB_raw_subscriber.py' and 'video_face2.py' will need to be moved from '/src/camera_pkg/scripts' to '/src/main/face_detection'. The file 'video_face2.py' will replace the original 'video_face.py' file in this folder.

Use the astrapro.launch file to start the astra camera for use. Run this command in the terminal to launch the camera:
```
roslaunch astra_camera astrapro.launch
```

Follow the instructions here to calibrate the camera: http://wiki.ros.org/camera_calibration/Tutorials/MonocularCalibration

**To run the program, run the file 'video_face2.py'**




  
  
