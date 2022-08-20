#!usr/bin/python

import socket
import hashlib
import time


def hextobyte(hex):
    return bytes.fromhex(hex)

def md5(hex):
    return hashlib.md5(hextobyte(hex)).hexdigest()

def gen_packet(data):
    magic = '2131'
    length = hex(int(len(data)/2 + 32))[2:].rjust(4, "0");
    unknown = '00000000'
    device_type = '0000'
    device_id = '0000'
    ts = hex(round(time.time()))[2:].rjust(8, "0");

    token = '2560f5ab98edbed5a67062108c50bb33'
    key = md5(token)
    iv = md5(key + token)

    packet = [magic, length, unknown, device_type, device_id, ts, token, data]
    checksum = md5("".join(packet))
    packet[6] = checksum    

    return ''.join(packet)

pp = gen_packet('afe0e9c5e26a2a26bbba23bd452e487e47e227086b5d55aac62949c533e0ea44782fde3e3f1d235eff60e25b31c8fa77')
print(pp, len(pp))
pp = hextobyte(pp)
# print(pp)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udp_host_src = sock.getsockname()[0]
udp_port_src = 12345                           

sock.bind((udp_host_src, udp_port_src))

udp_host_des = "192.168.0.50"
udp_port_des = 54321

msg = bytes.fromhex('21310020ffffffffffffffffffffffffffffffffffffffffffffffffffffffff');

sock.sendto(pp, (udp_host_des, udp_port_des))

print("Waiting for Response...")
data,addr = sock.recvfrom(1024)     
print("Received Messages form:", addr, end='\n\n')

print(data.hex())

print()
print()
