import socket
from miio_data import *
from config import token as TOKEN
from utils import *
from aes import encrypt, decrypt

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind(("", 12345))

sock.sendto(hex_to_byte(HELLO_PACKET), ('255.255.255.255', 54321))
data, addr = sock.recvfrom(1024)
print('Received from:', addr)
data = data.hex()
# print(data)

# packet_payload = encrypt(GET_TIMER_DATA)
# packet_payload = encrypt(GET_INFO_DATA)
packet_payload = encrypt(GET_POWER_STATUS_DATA)
# packet_payload = encrypt(POWER_OFF_DATA)
# packet_payload = encrypt(POWER_ON_DATA)

packet_length = hex(len(packet_payload) + 32)[2:].rjust(4, '0')
packet_head = hex_to_byte( data[:4] + packet_length + data[8:32] + TOKEN )

packet = bytearray(packet_head + packet_payload)

packet_checksum = md5(packet)

for i in range(0, 16):
    packet[i+16] = packet_checksum[i]

print('Final Packet: ')
print(packet.hex())

sock.sendto(packet, addr)
data, addr = sock.recvfrom(1024)
print('Received from:', addr)

data = data.hex()
decrypt(data[64:])