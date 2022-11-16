import cv2
from pyzbar.pyzbar import decode
import time
import glob
import cv2
import pandas as pd
import pathlib
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
valid_code=[]
used_decode=[]
camera=True
with camera==True:
    success,frame=cap.read()
    for code in decode(frame):
        if code.data.decode('utf-8') is not  used_decode:
            print("pass")
            print(code.data.decode('utf-8'))
            used_decode.append(code.data.decode('utf-8'))
            time.sleep(2)
        elif  code.data.decode('utf-8')  in used_decode:
              print("pass")
              time.sleep(2)
        else:
            cv2.show("hello".frame)
            cv2.waitKEY(1)
              