import socket
import hashlib

def hex_to_byte(hex: str) -> bytes:
    return bytes.fromhex(hex)

def md5(data: bytes) -> bytes:
    return hashlib.md5(data).digest()

TOKEN = '2560f5ab98edbed5a67062108c50bb33'
HELLO_PACKET = '21310020ffffffffffffffffffffffffffffffffffffffffffffffffffffffff'
GET_INFO_DATA = '5edc00f3fd2d5d3bec1c5ff56e78e2645fc529220e5f09e59f4d9bb58762ef5f9620fa9d2215ec0621b71075d2cd7f2d'
GET_POWER_STATUS_DATA = 'afe0e9c5e26a2a26bbba23bd452e487e47e227086b5d55aac62949c533e0ea44782fde3e3f1d235eff60e25b31c8fa77'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind(("0.0.0.0", 12345))

sock.sendto(bytes.fromhex(HELLO_PACKET), ('255.255.255.255', 54321))
data, addr = sock.recvfrom(1024)
print('Received from:', addr)

data = data.hex()
print(data)

# packet_payload = hex_to_byte(GET_INFO_DATA)
packet_payload = hex_to_byte(GET_POWER_STATUS_DATA)
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
print(data)

