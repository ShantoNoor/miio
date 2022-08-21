import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind(("0.0.0.0", 12345))

sock.sendto(bytes.fromhex('21310020ffffffffffffffffffffffffffffffffffffffffffffffffffffffff'), ('255.255.255.255', 54321))
data, addr = sock.recvfrom(1024)
print('Received from:', addr)
print(data.hex())

sock.sendto(bytes.fromhex('21310020ffffffffffffffffffffffffffffffffffffffffffffffffffffffff'), addr)
data, addr = sock.recvfrom(1024)
print('Received from:', addr)
print(data.hex())

