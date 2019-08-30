#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: santiago
"""


file_original=["train.txt","val.txt","trainval.txt","test.txt"]
file_append=["train_append.txt","val_append.txt","trainval_append.txt","test_append.txt"]


#c denotes content
#a denotes append file
#o denotes original file


for i in range(4):
    print(i)
    o=open(file_original[i],'a')
    a=open(file_append[i],'r')
    ac=a.readlines() #all 
    o.writelines(ac)
    o.close() 
    a.close()
