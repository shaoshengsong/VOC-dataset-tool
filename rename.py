#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:27:25 2019

@author: santiago
"""

import os
path = "/img"
filelist = os.listdir(path) #include file and folder
count=9964

for file in filelist:   
    old_dir=os.path.join(path,file)  
    if os.path.isdir(old_dir):   
        continue
    filename=os.path.splitext(file)[0]   
    filetype=os.path.splitext(file)[1]  
    new_dir=os.path.join(path,str(count).zfill(6)+filetype)  
    os.rename(old_dir,new_dir)
    count+=1


print(path)

