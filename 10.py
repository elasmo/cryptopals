#!/usr/bin/env python3
#
# Challenge 10: Implement CBC mode
#
from sys import argv, exit
from os.path import basename
from cryptopals import aes_cbc_enc
from cryptopals import aes_ecb_dec

from Crypto import Random

if len(argv) <= 1:
    print("Usage: {} <filename>".format(basename(argv[0])))
    exit(1)

if __name__ == "__main__":
    """
    filename = argv[1]
    block_size = 16
    key = b"YELLOW SUBMARINE"
    iv = b'\x00' * block_size
    ciphertext = b""

    with open(filename, "rb") as fo:
        while True:
            block = fo.read(block_size)

            if not block:
                break

            ciphertext += aes_cbc_enc(block, key, iv)

    print(ciphertext)
    """

    plaintext = b"blahblah0123askdsadklasdsak"
    key = b"YELLOW SUBMARINE"
    iv = Random.new().read(16) 
    ciphertext = aes_cbc_enc(plaintext, key, iv)

    print("Plaintext\t", plaintext)
    print("Key\t", key)
    print("IV\t", iv)
    print("Ciphertext\t", ciphertext)
    print("Decrypted\t", aes_ecb_dec(ciphertext, key))

