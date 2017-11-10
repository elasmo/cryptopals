#!/usr/bin/env python3
#
# Challenge 5: Implement repeating-key XOR
#
from sys import argv, exit
from os.path import basename
import binascii

if len(argv) <= 1:
	print("Usage: {} <filename>".format(basename(argv[0])))
	exit(0)


# XOR 3-byte input block with a 3-byte key
def encrypt(blk, key):
	if len(key) != 3 or len(blk) != 3:
		raise ValueError("out of range")

	buf = ""
	for m, k in zip(key, blk):
		buf += chr(ord(m)^ord(k))

	return buf
		
ciphertext = ""
filename = argv[1]
key = "ICE"

with open(filename, 'r', encoding='utf-8') as fo:
	while True:
		chunk = fo.read(len(key))

		if not chunk:
			break

		print("Processing '" + chunk + "'")

		ciphertext += encrypt(chunk, key)

print("Encrypted:")
print(''.join('{:02x}'.format(ord(c)) for c in ciphertext))
