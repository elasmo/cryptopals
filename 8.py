#!/usr/bin/env python3
#
# Challenge 8: Detect AES in ECB mode
#
from cryptopals import split_string
from cryptopals import detect_aes_ecb

with open("8.txt", 'rb') as f:
	block_size = 16
	uniq_blocks = 0
	
	eylen = 0
	oldlen = 1337
	for ciphertext in f:
		uniqs = set(split_string(ciphertext.strip(b'\n'), block_size))

		n_uniqs = len(uniqs)
		if n_uniqs < oldlen:
			eylen = ciphertext
			oldlen = n_uniqs
			
	print("Probably encrypted in AES ECB m0de: {:}\n".format(eylen))
