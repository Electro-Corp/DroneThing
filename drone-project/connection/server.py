import socket
import os
import time
HOST = ''
PORT = 6000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST,PORT))
	s.listen(1)
	#s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSERADDR,1)
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
	print("Connection: ",addr)
	i = 0
	parts = []
	while True:
		
		while True:
			
			#print("reciving")
			data = conn.recv(350000)
			#conn.sendall(bytearray(data))
			#data = data.decode()
			
			#while not data:
		#		data = conn.recv(10000)
			#print("done")
			if not data:
				print("AVERAGE: "+str(sum(parts)/len(parts)))
				frames = 0 
				break
			#print("writing")
			#os.system("rm recived.jpg")
			b = bytearray(data)
			
			#print(bytearray(data))
			#print(data)
			if(data == bytearray([0xf8])):
				print("NEXT FRAME")
				frames = frames + 1
				if ( i != 0):
                                	parts.append(i)
				i = 0
				
				break		
			#print(str(b[len(b)-1]))
			#if(b[len(b)-1] ==248):
		#		print("NEXT FRAME REAL")
	#			frames = frames +1
#				break
			with open('images/recived'+str(frames)+'.jpg','ab') as r:
					#if(prevdata != data and isboi == 1):
				
				print("RECIVING DATA "+str(frames)+" PART: "+str(i))
				i = i + 1
				
				r.write(bytearray(data))

			prevdata = data
			
			
		#print("Finished")
