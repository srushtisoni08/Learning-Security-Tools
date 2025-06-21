#!/bin/python3

import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid number of arguments")

print("-" * 50)
print("Scanning target : " + target)
print("Time : " + str(datetime.now()))
print("-" * 50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print(f"port {port} is open")
		s.close()
		
except keyboardInterrupt:
	print("Exiting System...")
	sys.exit()

except socket.gaierror:
	print("Host Name could not be resolved")
	sys.exit()

except socket.error:
	print("Could Not Connect To Server")
	sys.exit()
