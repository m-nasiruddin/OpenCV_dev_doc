#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 18:57:53 2018

@author: osboxes
"""

import cv2

img = cv2.imread('images/input/home.jpg',0)
## check opencv version and construct the detector
is_cv3 = cv2.__version__.startswith("3.")
if is_cv3:
    detector = cv2.SimpleBlobDetector_create()
else:
    detector = cv2.SimpleBlobDetector()

## detect 
kpts = detector.detect(img)
