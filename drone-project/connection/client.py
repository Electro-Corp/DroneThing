import socket
import os
import numpy as np
import time
print("Client")
from picamera import PiCamera
try:
    import cv2
except:
    print("CV2 Load failure, not a problem *if* you have a PiCam. If you dont, sad")
    if(str(input("Would you like to install it now? (y/n)")) == "y"):
        os.system("pip3 install opencv-contrib-python")

HOST = '192.168.86.35'
print("Connecting to: "+HOST)
PORT = 8080
try:
    camera = PiCamera()
    camera.resolution = (1024,720)
    camera.start_preview()
except:
    cam = cv2.VideoCapture(0)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #while True:
    for b in range(2):
        print("taking and sending...")
        try:
            camera.capture('test.jpg')
        except:
            ret, image = cam.read()
            
            cv2.imwrite('/home/segfault/DroneThing/drone-project/connection/test.jpg',image)
            
        with open('test.jpg',"rb") as image:
            f = image.read()
            b = bytearray(f)
            s.sendall(b)
        print("Done!")
        print(len(b))
        time.sleep(0.4)
cam.release()