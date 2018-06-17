#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 16:24:26 2018

@author: osboxes
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()  # capture frame-by-frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # our operations on the frame come here
    cv2.imshow('frame', gray)  # display the resulting frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# when everything done, release the capture
cap.release()
cv2.destroyAllWindows()
