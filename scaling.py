#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:57:03 2018

@author: osboxes
"""

import cv2

img = cv2.imread('images/input/messi5.jpg')
res = cv2.resize(img, None, fx = 2, fy = 2, interpolation = cv2.INTER_CUBIC)
# OR
height, width = img.shape[ :2]
res = cv2.resize(img, (2*width, 2*height), interpolation = cv2.INTER_CUBIC)
