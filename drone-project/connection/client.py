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
PORT = 6000
resodiv = 1
frames = 50
try:
    camera = PiCamera()
    camera.resolution = (1024,720)
    camera.start_preview()
except:
    cam = cv2.VideoCapture(0)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #while True:
    for g in range(1):
        print("taking and sending...")
        try:
            camera.capture('img.jpg')
        except:
            cam.set(cv2.CAP_PROP_FRAME_WIDTH,480/resodiv)
            cam.set(cv2.CAP_PROP_FRAME_HEIGHT,360/resodiv)
            #based = 0
            for i in range(frames):
                ret, image = cam.read()
                try:
                    cv2.imwrite('/home/segfault/DroneThing/drone-project/connection/img'+str(i)+'.jpg',image)
                except:
                    print("Failed at: " + str(i))
                print("Took: "+str(i))

        for i in range(frames):
            with open('img'+str(i)+'.jpg',"rb") as image:
                f = image.read()
                b = bytearray(f)
 
                s.sendall(b)
                print("Sending: "+str(i))
                time.sleep(0.01)
                based = 0xf8
                
                s.sendall(bytearray([based]))
                
                print("Confirm bit: "+ str(bytearray([based])))
                count = 0
                time.sleep(0.01)
                
                
        print("Done!")
        print(len(b))
        #based = bytearray([0x00])
        #s.sendall(based)
        time.sleep(0.4)
cam.release()