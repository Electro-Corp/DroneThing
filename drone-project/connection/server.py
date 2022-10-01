import socket
import os
import time
HOST = ''
PORT = 6000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # establish 
	s.bind((HOST,PORT)) #create socket
	s.listen(1) #listen for connection

	conn, addr = s.accept()

	isboi = 0
	try:
		os.system("rm recived.jpg")
	except:
		pass
	
	#with conn:
	frames = 0
	print("Connection: ",addr)
	i = 0
	parts = []
	while True:
		
		while True:
			data = conn.recv(350000)
			if not data:
				print("AVERAGE: "+str(sum(parts)/len(parts)))
				frames = 0 
				break
			b = bytearray(data)
			if(data == bytearray([0xf8])):
				print("NEXT FRAME")
				frames = frames + 1
				if ( i != 0):
                                	parts.append(i)
				i = 0
				
				break		

			with open('images/recived'+str(frames)+'.jpg','ab') as r:

				
				print("RECIVING DATA "+str(frames)+" PART: "+str(i))
				i = i + 1
				
				r.write(bytearray(data))

			prevdata = data
			
			

