#!/usr/bin/env python3
#
# Challenge 6: Break repeating-key XOR ("Vigenére")
# 

from cryptopals import *
"""
from cryptopals import ham_distance
from cryptopals import split_string
from cryptopals import transp_blks
from cryptopals import single_xor_dec
from cryptopals import repeating_xor_dec
from cryptopals import count_chars
from cryptopals import calc_score
from cryptopals import guess_keylen
"""

from string import ascii_letters
from base64 import b64decode

data = open("6.txt", 'rb').read()
ciphertext = b64decode(data)

#print("Ciphertext:", ciphertext)

if __name__ == "__main__":
	# Find key length
	guessed_keylen = guess_keylen(ciphertext, 2, 40)
	print("Guessed key length:", guessed_keylen)

	# Split ciphertext in keylen n byte blocks and transpose 
	ciphertext_blocks = split_string(ciphertext, guessed_keylen)
	ciphertext_transp = transp_blks(ciphertext_blocks)

	# Decrypt transposed ciphertext blocks using key ascii 0-255
	# ..and try find key that harvest the best scores
	guessed_key = ""

	for i in range(len(ciphertext_transp)):
		score = old_score = 0
		key_part = ""

		for key in range(0, 255):
			plaintext = single_xor_dec(ciphertext_transp[i], key)

			freq  = count_chars(plaintext)
			score = calc_score(freq)

			if(score > old_score):
				old_score = score
				key_part = chr(key)

		guessed_key += key_part

	print("Encryption key: " + guessed_key)

	# Finally!
	deciphered = ""
	for i in range(len(ciphertext_blocks)):
		deciphered += repeating_xor_dec(ciphertext_blocks[i], guessed_key)

	print("Dechiphered:\n" + deciphered)
