#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 15:22:43 2018

@author: osboxes
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/input/home.jpg',0)
plt.hist(img.ravel(),256,[0,256]); plt.show()
