#!/usr/bin/env python3
#
# Challenge 7: AES in ECB mode
#
from cryptopals import aes_ecb_dec
from base64 import b64decode

if __name__ == "__main__":
    key = b"YELLOW SUBMARINE"

    with open("7.txt", "rb") as f:
        ciphertext = f.read()

    ciphertext = b64decode(ciphertext)
    plaintext  = aes_ecb_dec(ciphertext, key)

    print(plaintext)
