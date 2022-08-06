import socket
import os

HOST = ''
PORT = 8080
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST,PORT))
	s.listen(1)
	conn, addr = s.accept()
	#data = conn.recv(350000)
	#prevdata = data
	isboi = 0

	os.system("rm recived.jpg")
	
	with conn:
		print("Connection: ",addr)
		while True:
			
			print("reciving")
			data = conn.recv(350000)
			#data = data.decode()
			
			#while not data:
		#		data = conn.recv(10000)
			print("done")
			if not data: break
			print("writing")
			#os.system("rm recived.jpg")
			b = bytearray(data)
			i = 0
			if(isboi == 0):
				pass
				#while(bytearray[i] != 0xff):
					
					
			with open('recived.jpg','ab') as r:
				#if(prevdata != data and isboi == 1):
					
				r.write(bytearray(data))
				#r.write(data)
				#newdata = str(data).replace('b',"")
				#r.write(newdata.replace("'",""))
			print("done")
			print(data)
			
			prevdata = data
			#break
			#with open('recived.jpg','rb') as r:
				#print(r.readlines())
			#conn.sendall(data)
			
