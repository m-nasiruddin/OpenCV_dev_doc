#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 15:32:52 2018

@author: osboxes
"""

import cv2

img1 = cv2.imread('images/input/ml.png')
img2 = cv2.imread('images/input/opencv_logo.jpg')

dst = cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
