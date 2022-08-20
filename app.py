#!usr/bin/python

import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udp_host_src = sock.getsockname()[0]
udp_port_src = 12345                           

sock.bind((udp_host_src,udp_port_src))

udp_host_des = "192.168.0.50"
udp_port_des = 54321

msg = bytes.fromhex('21310020ffffffffffffffffffffffffffffffffffffffffffffffffffffffff');

sock.sendto(msg,(udp_host_des,udp_port_des))

print("Waiting for Response...")
data,addr = sock.recvfrom(1024)     
print("Received Messages:", "from", addr, end='\n\n')

print(data)

print()
print()
