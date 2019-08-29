#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: santiago
"""

import cv2
import os

count=9964 # save file name
filetype=".jpg"
save_img_directory = "/img/" 


video_file_path= "VID.mp4"
cap = cv2.VideoCapture(video_file_path)

while(1):
    ret,frame = cap.read()  
    if(ret):
        #cv2.imshow("capture",frame) 
        new_dir=os.path.join(save_img_directory,str(count).zfill(6)+filetype)  
        print(new_dir)
        cv2.imwrite(new_dir,frame)
    else:
        break

    count += 1
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break  
    
cap.release()
cv2.destroyAllWindows()
print("complete")