#!/usr/bin/env python3
import socket
import sys
from tqdm import tqdm


remoteServer    = input("Enter host to scan:     ")
serverIP  = socket.gethostbyname(remoteServer)

print('scanning...')


for port in tqdm(range(1,65535)):  
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((serverIP, port))
    if result == 0:
        print("Port {}: 	Open".format(port))
    elif result == 113:
        print("No route to host. Check connection.")
        sys.exit()
    sock.close()