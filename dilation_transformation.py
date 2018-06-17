#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 17:13:58 2018

@author: osboxes
"""

import cv2
import numpy as np

img = cv2.imread('images/input/j.png',0)
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(img,kernel,iterations = 1)
