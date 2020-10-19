  
#! /usr/bin/env python3

import socket, params, os, sys, re
from framedSock import framedSend, framedReceive
sys.path.append("../lib")  

switchesVarDefaults = (
	(('-l', '--listenPort') ,'listenPort', 50001),
	(('-d', '--debug'), "debug", False), # boolean (set if present)
	(('-?', '--usage'), "usage", False), # boolean (set if present)
	)

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def getFile():
	invalid = True
	while invalid:
		try:
			filename = input(str("Please enter the filename to send:"))
			file = open(filename,'rb')
			invalid = False
		except FileNotFoundError:
			print("I couldn't find your file! Please keep trying.")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	try:
		s.connect((HOST, PORT))
		file = getFile();
		
		data = file.read(1024)
		s.send(data)
		file.close()
	except ConnectionRefusedError:
		print("Could not connect to server!")