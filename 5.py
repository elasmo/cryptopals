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
	exit(0)

ciphertext = ""
filename = argv[1]
key = "ICE"

with open(filename, 'rb') as fo:
	while True:
		chunk = fo.read(len(key))

		if not chunk:
			break

		print("Processing '" + str(chunk) + "'")
		ciphertext += repeating_key_xor(chunk, key)

print("Encrypted:")
print(''.join('{:02x}'.format(ord(c)) for c in ciphertext))
