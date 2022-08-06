import socket
import os
import numpy as np
from picamera import PiCamera
HOST = '192.168.86.35'
PORT = 8080

camera = PiCamera()
camera.resolution = (1024,720)
camera.start_preview()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #while True:
    for b in range(4000):
        camera.capture('test.jpg')
        #os.system("sed 's/\x0//g' test1.jpg > test.jpg")
        """with open('test.jpg','rb') as t:
            #print(t.readlines())
            print("Reading..")
            b = t.readlines()
            for i in range(len(b)): print(b[i])
            #b.remove("x00")
            #b[:] = [x for x in b if x != 0x00]
            print("Array")
            a = np.array(b)
            print("sendng...")
            #result = bytearray([int(x,0) for x in b])
            s.sendall(bytes(result)) #a.tobytes())
            input("")
            print(a.tobytes())"""
        with open('test.jpg',"rb") as image:
            f = image.read()
            b = bytearray(f)
            #for i in range(len(b)):
            #    print(b[i])
            s.sendall(b)
            print(b)
        print("reciving")
        print(len(b))
        #data = s.recv(5000)
        #with open('gotback.jpg', 'wb') as r:
        #    r.write(data)
        #print("Data",repr(data))
    #while True:
    #    camera.capture('test.jpg')
    #    s.sendall(b'REAL????')
	#    data = s.recv(1024)
	#    print('Received', repr(data))
