#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 18:16:17 2018

@author: osboxes
"""

import cv2

img = cv2.imread('images/input/messi5.jpg')
# check if optimization is enabled
cv2.useOptimized()
%timeit res = cv2.medianBlur(img, 49)
