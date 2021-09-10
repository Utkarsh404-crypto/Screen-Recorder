from PIL import ImageGrab
import numpy as np
import cv2
import datetime
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
capture_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))     #it will create a frame of particular width and height and then it will store in a file.

while True:

    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img_np = np.array(img)      #this function takes image as input and then convert it to numpy array(value of each pixels)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow('Screen Recorder', img_final)
    capture_video.write(img_final)      #it will write the frame in the output file using this (capture_video) object.
    if cv2.waitKey(10) == ord('q'):
        break

