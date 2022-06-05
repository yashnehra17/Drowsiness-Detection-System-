# Drowsiness Detection OpenCV 😴 🚫 🚗
This code can detect your eyes and alert when the user is drowsy.

# Applications 🎯
This can be used by riders who tend to drive for a longer period of time that may lead to accidents
 

# Library required

1) import cv2
2) import imutils
3) import dlib
4) import time
5) import face_recognitation
6) import numpt
7) import thread


# Description 

A computer vision system that can automatically detect driver drowsiness in a real-time video stream and then play an alarm if the driver appears to be drowsy.

# Algorithm 

Each eye is represented by 6 (x, y)-coordinates, starting at the left-corner of the eye (as if you were looking at the person), and then working clockwise around the eye.

It checks 20 consecutive frames and if the Eye Aspect ratio is less than 0.25, Alert is generated.
