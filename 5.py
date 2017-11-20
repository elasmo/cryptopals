#!/usr/bin/env python3
#
# Challenge 5: Implement repeating-key XOR
#
from sys import argv, exit
from os.path import basename
from cryptopals import repeating_key_xor
import binascii

if len(argv) <= 1:
    print("Usage: {} <filename>".format(basename(argv[0])))
    exit(1)

if __name__ == "__main__":
    ciphertext = ""
    filename   = argv[1]
    key        = b"ICE"
    key_len    = len(key)

    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(key_len)

            if not chunk:
                break

            print("Processing", chunk)
            ciphertext += repeating_key_xor(chunk, key)

    print("Ciphertext:")
    print(''.join('{:02x}'.format(ord(c)) for c in ciphertext))
