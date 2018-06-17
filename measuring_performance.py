#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 18:08:05 2018

@author: osboxes
"""

import numpy as np
import cv2

img1 = cv2.imread('images/input/messi5.jpg')

e1 = cv2.getTickCount()
for i in np.xrange(5,49,2):
    img1 = cv2.medianBlur(img1,i)
e2 = cv2.getTickCount()
t = (e2 - e1)/cv2.getTickFrequency()
print(t)

# Result I got is 0.521107655 seconds
