#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: santiago
"""

import os  
import random  
  
trainval_percent = 0.8  
train_percent = 0.5  
xmlfilepath = '/annotations'  
txtsavepath = '/txt'  
total_xml = os.listdir(xmlfilepath)  # xml file name list
 
total_file_count=len(total_xml)  # file count

list=range(total_file_count)  

trainval_file_count=int(total_file_count*trainval_percent)  #trainval file count

train_file_count=int(trainval_file_count*train_percent)  #train file count


#random.sample([1, 2, 3, 4, 5],  3)  # Choose 3 elements
#[4, 1, 5]
#sample([10, 20, 30, 40, 50], k=4)    # Four samples without replacement
#[40, 10, 50, 30]

trainval= random.sample(list,trainval_file_count)  
train=random.sample(trainval,train_file_count)  
  
ftrainval = open(txtsavepath+'/trainval_append.txt', 'w')  
ftest = open(txtsavepath+'/test_append.txt', 'w')  
ftrain = open(txtsavepath+'/train_append.txt', 'w')  
fval = open(txtsavepath+'/val_append.txt', 'w')  
  
for i  in list:  
    name=total_xml[i][:-4]+'\n' # .xml 4 char
    if i in trainval:  
        ftrainval.write(name)  
        if i in train:  
            ftrain.write(name)  
        else:  
            fval.write(name)  
    else:  
        ftest.write(name)  
  
ftrainval.close()  
ftrain.close()  
fval.close()  
ftest .close()
