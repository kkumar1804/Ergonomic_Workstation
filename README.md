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

Use the astrapro.launch file to start the astra camera for use. Run this command in the terminal to launch the camera:
```
roslaunch astra_camera astrapro.launch
```

Follow the instructions here to calibrate the camera: http://wiki.ros.org/camera_calibration/Tutorials/MonocularCalibration


**Run the file 'video_face.py' to start the program**


This project used parts of code from this repo: https://github.com/vardanagarwal/Proctoring-AI
  
  
