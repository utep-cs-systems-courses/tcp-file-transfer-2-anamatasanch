#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	try:
		s.connect((HOST, PORT))
		s.sendall(b'Hello, world') #sends the message
		data = s.recv(1024) #recieves server message
		print('Received', repr(data))
	
	except ConnectionRefusedError:
		print("Could not connect to server!")

	

