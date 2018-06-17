#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 17:18:58 2018

@author: osboxes
"""

import cv2
import numpy as np

img = cv2.imread('images/input/j_noise2.png',0)
kernel = np.ones((5,5),np.uint8)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
