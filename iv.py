import hashlib

def hex_to_byte(hex: str) -> bytes:
    return bytes.fromhex(hex)


def md5(inp: bytes) -> bytes:
    m = hashlib.md5()
    m.update(inp)
    return m.digest()


def key_iv(token: bytes) -> (bytes, bytes):
    """Derive (Key, IV) from a Xiaomi MiHome device token (128 bits)."""
    key = md5(token)
    iv = md5(key + token)
    return (key, iv)


token = '3e96ea3477ef3fc2f1615144a37c57bd'

key = md5(hex_to_byte(token))
iv = md5(key + hex_to_byte(token))

print(key.hex())
print(iv.hex())
