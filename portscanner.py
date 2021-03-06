#!/bin/python3
           
import pyfiglet

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)


import sys
import socket
from datetime import datetime

#Defining a target
if len(sys.argv) ==2:
	target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4
else:
	print("Invalid ammount of Argument")

#Add Banner 

print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

try:
	for port in range(1,65535):     #will scan ports between 1 to 65,535
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #returns an error indicator
		if result ==0:
			print("Port {} is open".format(port))
		s.close()	
except KeyboardIntruppt:
		print("\n Exitting Program !!!!")
		sys.exit()
except socket.gaierror:
		print("\n Hostname Could Not Be Resolved !!!!")
		sys.exit()
except socket.error:
		print("\ Server not responding !!!!")
		sys.exit()
