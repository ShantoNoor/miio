import hashlib

def hex_to_byte(hex: str) -> bytes:
    return bytes.fromhex(hex)

def md5(data: bytes) -> bytes:
    return hashlib.md5(data).digest()