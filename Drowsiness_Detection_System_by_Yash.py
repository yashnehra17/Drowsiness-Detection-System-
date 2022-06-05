
from collections import Counter
from concurrent.futures import thread
from itertools import filterfalse
from lib2to3.pgen2.token import MINEQUAL
from pickle import FALSE, TRUE
import face_recognition
import cv2
import time
import distance as dist
import playsound
import _thread
import numpy as np

MIN_AER= 0.30
EYE_AR_COSEC_FRAMES = 10

COUNTER = 0
ALARAM_ON = False
def sound_alarm(soundfile):
    playsound.playsound(soundfile)

def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1],eye[5])
    B = dist.euclidean(eye[2],eye[5])
    C = dist.euclidean(eye[0],eye[3])
    ear = (A+B)/(2*C)
def main():
    global COUNTER,ALARAM_ON
    video_capture = cv2.VideoCapture(0)
    video_capture.set(3,320)
    video_capture.set(4,240)
    while True:
        ret,frame = video_capture.read()
        face_landmarks_list = face_recognition.face_landmarks(frame)
        for face_landmark in face_landmarks_list:
            leftEye = face_landmark["left_eye"]
            rightEye = face_landmark["right_eye"]

            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)
            ear = (leftEAR + rightEAR)/2

            lpts = np.array(leftEye)
            rpts = np.array(rightEye)

            cv2.polylines(frame,[lpts],True, (255,255,0),1)
            cv2.polylines(frame,[rpts],True, (255,255,0),1)

            if ear<MIN_AER:
                COUNTER+= 1
                if COUNTER>= EYE_AR_COSEC_FRAMES:
                    if not ALARM_ON:
                        ALARM_ON = True
                        t = thread(target =sound_alarm, args = ('alarm.wav,'))
                        t.daemon = True
                        t.start()
                cv2.putText(frame,"Alert! you are feeling asleep",(5,10),cv2.FRONT_SIMPLEX,0.4,(0,0,255),1)
            else:
                    COUNTER=0
                    ALARAM_ON=False
            cv2.putText(frame,"Ear:.2f".format(ear),(300,10), cv2.FRONT_HERSHEY_SIMPLEX,0.4,(0,0,255),1)
            cv2.imshow("sleep Detection",frame)
            if cv2.waitKey(1)==ord('q'):
                 break
        video_capture.release()
        cv2.destroy.ALLWindows()

def new_func(frame):
    cv2.putText(frame,"Alert! you are feeling asleep",(5,10),cv2.FRONT_HERSHEY_SIMPLEX,0.4,(0,0,255),1)
