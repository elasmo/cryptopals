#!/usr/bin/env python3
#
# Challenge 10: Implement CBC mode
#
from sys import argv, exit
from os import urandom
from os.path import basename
from cpals import aes_cbc_enc, aes_cbc_dec
from base64 import b64decode

if len(argv) <= 1:
    print("Usage: {} <filename>".format(basename(argv[0])))
    exit(1)

if __name__ == "__main__":
    key = b'YELLOW SUBMARINE'
    iv = b'\x00' * 16

    with open(argv[1], 'r') as f:
        ciphertext = f.read()
    print(aes_cbc_dec(b64decode(ciphertext), key, iv))
