#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 14:31:26 2019

@author: santiago
"""

import os
import cv2


 
path = "/img/"

 
for filename in os.listdir(path):
    if os.path.splitext(filename)[1] == '.png':
        print(path + filename)
        img = cv2.imread(path + filename)
        print(filename.replace(".png",".jpg"))
        newfilename = filename.replace(".png",".jpg")
        cv2.imwrite(path + newfilename,img)


