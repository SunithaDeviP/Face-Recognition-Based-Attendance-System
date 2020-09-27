import tkinter as tk
import tkinter.ttk as ttk
import time

import os
import cv2
from PIL import Image, ImageEnhance 

rootdir = '/home/q8/Desktop/FINAL_YEAR_PROJECT/user_raw_dataset/'
destination = '/home/q8/Desktop/FINAL_YEAR_PROJECT/FaceRecognition/train_img/'


def blur_image(img,path,count):
    blur_value = [12,13,14,15]
    for value in blur_value:
        avging = cv2.blur(img,(value,value)) 
        cv2.imwrite(path+'/img'+str(count)+'.png',avging)
        count+=1
    return count

def brightness(img_path,path,count):
    img = Image.open(img_path)
    brightness_value=[0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4]
    for value in brightness_value:
        enhancer = ImageEnhance.Brightness(img)
        enhanced_im = enhancer.enhance(value)
        enhanced_im.save(path+'/img'+str(count)+'.png')
        count+=1
    return count

def replicate_original_image(img,path,count):
    i =0
    #img = cv2.imread(img_path)
    for i in range(10):
        cv2.imwrite(path+'/img'+str(count)+'.png',img)
        count+=1
    return count

def generate_dataset():
    for subdir, dirs, files in os.walk(rootdir):
        count=0
        inc =0
        print("INC ",inc)
        dest = destination + os.path.basename(subdir)
        try:
            os.makedirs(dest)    
        except FileExistsError:
            return
        for file in files:
            img = cv2.imread(os.path.join(subdir,file))
            #print(img)
            count = blur_image(img,dest,count)
            count = replicate_original_image(img,dest,count)
            count = brightness(os.path.join(subdir,file),dest,count)
        dest=destination
    cv2.destroyAllWindows() 

#generate_dataset()