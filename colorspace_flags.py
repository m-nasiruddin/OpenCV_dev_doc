#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 19:04:16 2018

@author: osboxes
"""

import cv2

flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)
