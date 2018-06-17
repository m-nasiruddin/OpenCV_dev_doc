#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 15:15:20 2018

@author: osboxes
"""

import cv2
import numpy as np

x = np.uint8([250])
y = np.uint8([10])

print(cv2.add(x,y)) # 250+10 = 260 => 255

print(x+y)          # 250+10 = 260 % 256 = 4
