from config import token
from Crypto.Cipher import AES
from utils import *

def key_iv(token: bytes) -> (bytes, bytes):
    """Derive (Key, IV) from a Xiaomi MiHome device token (128 bits)."""
    key = md5(token)
    iv = md5(key + token)
    return (key, iv)


'''
if token == '2560f5ab98edbed5a67062108c50bb33' then,
    Key == 08d08f856294be9f2d8b90154cdc7ac5
    IV == 33b8c012ec96b715c16b26d5033c477b
    get_info_data_hex_str == '5edc00f3fd2d5d3bec1c5ff56e78e2645fc529220e5f09e59f4d9bb58762ef5f9620fa9d2215ec0621b71075d2cd7f2d'
    get_info_data_bytes ==  b'{"method":"miIO.info","params":[],"id":1}'
'''

key = md5(hex_to_byte(token))
iv = md5(key + hex_to_byte(token))

def encrypt(plaintext: bytes, block_size = 16) -> bytes:
    # Create the AES cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Pad the plaintext using PKCS#7 padding
    padding_length = block_size - len(plaintext) % block_size
    padding = bytes([padding_length]) * padding_length
    padded_plaintext = plaintext + padding

    # Encrypt the padded plaintext
    ciphertext = cipher.encrypt(padded_plaintext)

    # Print the results
    # print('Key:', key.hex())
    # print('IV:', iv.hex())
    # print('Plaintext:', plaintext)
    # print('Padded plaintext:', padded_plaintext)
    print('Ciphertext:', ciphertext.hex())

    return ciphertext

def decrypt(ciphertext_hex: str, block_size = 16) -> bytes:
    # Create the AES cipher object
    cipher = AES.new(key, AES.MODE_CBC, iv)

    ciphertext = hex_to_byte(ciphertext_hex)
    # Decrypt the ciphertext
    padded_plaintext = cipher.decrypt(ciphertext)

    # Unpad the plaintext by removing the padding bytes
    padding_length = padded_plaintext[-1]
    plaintext = padded_plaintext[:-padding_length]

    # Print the results
    # print('Token:', token)
    # print('Key:', key.hex())
    # print('IV:', iv.hex())
    # print('Ciphertext:', ciphertext.hex())
    # print('Padded plaintext:', padded_plaintext)
    print('Plaintext:', plaintext)

    return plaintext
