#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 14:34:13 2018

@author: osboxes
"""

import cv2

# blow program loads an image in grayscale, displays it, save the image if you
# press ‘s’ and exit, or simply exit without saving if you press ESC key
img = cv2.imread('images/input/messi5.jpg', 0)  # read the image
cv2.namedWindow('image', cv2.WINDOW_NORMAL)  # create window
cv2.imshow('image', img)  # display the image
k = cv2.waitKey(0) & 0xFF  # keyboard binding function
if k == 27:  # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):  # wait for 's' key to save and exit
    cv2.imwrite('images/output/messigray.png', img)  # save the image in PNG format
    cv2.destroyAllWindows()  # destroys all wondows we created
