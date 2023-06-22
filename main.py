from EdgeFinderV4 import BoundaryDetector as BD
from ImageFrame import Frame
from controll_angle_functions import get_angle
from hardwareControl import send
from MAfilter import FIR_filter
#import cv2 as cv
import numpy as np
from picamera2 import Picamera2
import libcamera

#resolution
width = 1280
height = 720
frame1 = Frame(width,height,5,height/2,height)
kernel = [-1,-1,-1,0,1,1,1]
myFilter = FIR_filter(5)
#setting camera and frame
picam2 = Picamera2()
preview_config = picam2.create_preview_configuration(main={"format": 'BGR888','size':(width,height)})
preview_config["transform"] = libcamera.Transform(hflip=1, vflip=1)
picam2.configure(preview_config)
picam2.start()

print('Program Start.')
counter_i = 0
def main():
    while True:
        #capture image
        image = picam2.capture_image("main")
        image.save('./saveimage/img'+str(counter_i)+'.jpg')
        counter_i += 1
        #save image
        #boundary detection
        B = BD(np.array(image)[:,:,0],kernel,frame1,90)
        #angle calculation
        P = get_angle(B,width,height)
        #MAfilter
        A = myFilter.updata(np.mean(P[1]))
        #send control
        send(A,255/2)
        #debug
    