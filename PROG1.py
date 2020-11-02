# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 16:38:23 2020

@author: SIDDHARTH RAJ DASH
"""


import cv2

videoCaptureObject = cv2.VideoCapture(0)
result = True
while(result):
    ret,frame = videoCaptureObject.read()
    cv2.imwrite("./input/NewPicture.jpg",frame)
    result = False
videoCaptureObject.release()
cv2.destroyAllWindows()