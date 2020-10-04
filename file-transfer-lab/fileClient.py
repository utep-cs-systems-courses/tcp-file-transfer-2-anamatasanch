#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	try:
		s.connect((HOST, PORT))
		filename = input(str("Please enter the filename to send:"))
		file = open(filename,'rb')
		data = file.read(1024)
		s.send(data)
		file.close()
	except ConnectionRefusedError:
		print("Could not connect to server!")