import socket
import os
import time
HOST = ''
PORT = 6000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST,PORT))
	s.listen(1)
	conn, addr = s.accept()
	#data = conn.recv(350000)
	#prevdata = data
	isboi = 0
	try:
		os.system("rm recived.jpg")
	except:
		pass
	
	#with conn:
	frames = 0
	while True:
		#print("Connection: ",addr)
		while True:
			
			#print("reciving")
			data = conn.recv(350000)
			#conn.sendall(bytearray(data))
			#data = data.decode()
			
			#while not data:
		#		data = conn.recv(10000)
			#print("done")
			if not data:
				frames = 0 
				break
			#print("writing")
			#os.system("rm recived.jpg")
			b = bytearray(data)
			i = 0

			if(data == bytearray([0xf8])):
				print("NEXT FRAME")
				frames = frames + 1
				break		
			
			with open('images/recived'+str(frames)+'.jpg','ab') as r:
					#if(prevdata != data and isboi == 1):
				
				print("RECIVING DATA "+str(frames))
				#print(bytearray(data))
				r.write(bytearray(data))

			prevdata = data
			
			
		#print("Finished")
