#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 12:01:21 2018

@author: osboxes
"""

import cv2
# to list all the available lists available
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)
