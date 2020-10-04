#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()		#listen for incoming conns
	conn, addr = s.accept()
	with conn:
		while True:
			print('Connected by', addr)
			filename = input(str("Please enter a file name for the incoming file"))
			file = open(filename, 'wb')
			data = conn.recv(1024)
			if not data:
				break
			file.write(data)
			file.close()
			print("File recieved and saved!")
			conn.sendall(data)