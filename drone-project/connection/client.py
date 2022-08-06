import socket

HOST = '192.168.86.34'
PORT = 8080
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:

	    s.sendall(b'REAL????')
	    data = s.recv(1024)
	    print('Received', repr(data))
