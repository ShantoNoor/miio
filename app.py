#!usr/bin/python

import socket
import hashlib
import time
import struct


def hb(hex):
    return bytes.fromhex(hex)

def md5(data):
    return hashlib.md5(data).digest()

# def gen_packet(data):
#     magic = '2131'
#     length = hex(int(len(data)/2 + 32))[2:].rjust(4, "0");
#     unknown = '00000000'
#     device_type = '0000'
#     device_id = '87942805'
#     ts = hex(round(time.time()))[2:].rjust(8, "0");

#     token = '2560f5ab98edbed5a67062108c50bb33'
#     key = md5(token)
#     iv = md5(key + token)

#     packet = [magic, length, unknown, device_type, device_id, ts, token, data]
#     print(hb("".join(packet)))
#     checksum = md5("".join(packet))
#     packet[6] = checksum    

#     return ''.join(packet)

def gen_packet(data):
    def init_msg_head(stamp: int, token: bytes, packet_len: int) -> bytes:
        print(stamp)
        head = struct.pack(
            '!BBHIII16s',
            0x21, 0x31,  # const magic value
            packet_len,
            0,  # unknown const
            0x053de695,  # unknown const
            0x000035ad,
            token  # overwritten by the MD5 checksum later
        )
        return head

    token = hb('2560f5ab98edbed5a67062108c50bb33')
    payload = hb(data)
    packet_len = len(payload) + 32
    packet = bytearray(init_msg_head(round(time.time()), token, packet_len) + payload)
    checksum = md5(packet)
    for i in range(0, 16):
        packet[i+16] = checksum[i]
    print(len(packet))
    return packet

# pp = gen_packet('afe0e9c5e26a2a26bbba23bd452e487e47e227086b5d55aac62949c533e0ea44782fde3e3f1d235eff60e25b31c8fa77')
pp = gen_packet('5edc00f3fd2d5d3bec1c5ff56e78e2645fc529220e5f09e59f4d9bb58762ef5f9620fa9d2215ec0621b71075d2cd7f2d')
print(pp.hex(), len(pp))
# pp = hb(pp)
# print(pp)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

udp_host_src = sock.getsockname()[0]
udp_port_src = 12345                           

sock.bind((udp_host_src, udp_port_src))

udp_host_des = "192.168.0.50"
udp_port_des = 54321

msg = bytes.fromhex('21310020ffffffffffffffffffffffffffffffffffffffffffffffffffffffff');

sock.sendto(msg, (udp_host_des, udp_port_des))

print("Waiting for Response...")
data,addr = sock.recvfrom(1024)     
print("Received Messages form:", addr, end='\n\n')

print(data.hex())

print()
print()

sock.sendto(pp, (udp_host_des, udp_port_des)) 
print("Waiting for Response...")
data,addr = sock.recvfrom(1024)
print("Received Messages form:", addr, end='\n\n')

print(data.hex())

print()
print()
