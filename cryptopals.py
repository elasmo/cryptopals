#!/usr/bin/env python3
#
# Used for cryptopal challenges 
# nov-2017
#
# Dependencies:
# * py36-pycrypto
# 
import base64
import binascii
from string import ascii_lowercase
from Crypto.Cipher import AES

# Letter frequency in english text
freq_en = { 
    'a' : 8.167, 'b' : 1.492, 'c' : 2.782, 'd' : 4.253, 'e' : 12.702,
    'f' : 2.228, 'g' : 2.015, 'h' : 6.094, 'i' : 6.966, 'j' : 0.153, 
    'k' : 0.772, 'l' : 4.025, 'm' : 2.406, 'n' : 6.749, 'o' : 7.507, 
    'p' : 1.929, 'q' : 0.095, 'r' : 5.987, 's' : 6.327, 't' : 9.056, 
    'u' : 2.758, 'v' : 0.978, 'w' : 2.360, 'x' : 0.150, 'y' : 1.974, 
    'z' : 0.074, ' ' : 4.025
}

# Perform frequency analysis and correlate with english language freq and return score
def calc_score(freqs):
	score = 0
	for char, occur in freqs.items():
		score += freq_en[char] + occur

	return score

# Count ascii letters im a string
def count_chars(text):
	freqs = dict.fromkeys(ascii_lowercase, 0)
	freqs.update({' ' : 0})
	
	for c in text.lower():
		val = ord(c)
		if val >= ord('a') and val <= ord('z') or val == ord(' '):
			freqs[c] += 1

	return freqs

# Guess key length
def guess_keylen(ciphertext, minlen, maxlen):
	hamdist_avg_old = maxlen
	guessed_keylen = 0

	for keylen in range(minlen, maxlen+1):
		offset_start = keylen
		offset_end = offset_start * 2

		# The length of n bytes with smallest hamming distance is probably
		# the length of the key.
		# Compare the first block of n bytes with the follow blocks and
		# calculate an average.

		hamdist_list = []
		max_blocks = round(len(ciphertext)/keylen, 0)

		while offset_end/keylen < max_blocks:
			blk_one = ciphertext[:keylen]
			blk_two = ciphertext[offset_start:offset_end]

			offset_start = offset_end
			offset_end += keylen

			hamdist_list.append(ham_distance(blk_one, blk_two)/keylen)

		# Calculate an average hamming distance for the current key length
		hamdist_avg = sum(hamdist_list)/len(hamdist_list)
		if(hamdist_avg < hamdist_avg_old):
			guessed_keylen = keylen
			hamdist_avg_old = hamdist_avg

	return guessed_keylen

# Calculate hamming distance between two strings
def ham_distance(str1, str2):
	if len(str1) != len(str2):
		raise ValueError("Strings not of equal length")

	distance = 0
	for a, b in zip(str1, str2):
		distance += bin(a^b).count('1')

	return distance

# Convert a hexadecimal string to base64
def hexstr_to_b64(text):
	return base64.b64encode(binascii.unhexlify(text))

# Take two equal-length buffers and produce their XOR combination
def hexstr_xor(str1, str2):
	if len(str1) != len(str2):
		raise ValueError("Strings not of equal length")

	hex_one = binascii.unhexlify(str1)
	hex_two = binascii.unhexlify(str2)

	result = ""
	for c in range(len(hex_one)):
		result += chr(hex_one[c]^hex_two[c])

	# str.encode returns a utf-8 encoded (default) bytes object
	return binascii.hexlify(str.encode(result))

# Split a string into blocks
def split_string(text, block_size):
	return [text[i:i+block_size] for i in range(0, len(text), block_size)]

# Transpose blocks: make a block that is the first byte of every block, 
# and a block that is the second byte of every block, and so on. 
def transp_blks(blks):
	transp_list = []

	keylen = len(blks[0])
	for char in range(keylen):
		buf = bytes()
		for i in range(len(blks)):
			buf += blks[i][char:char+1]

		transp_list.append(buf)

	return transp_list

# Repeating-XOR decipher
def repeating_xor_dec(ciphertext, key):
	if len(ciphertext) != len(key):
		# XXX: should I use padding instead(?)
		key = key[0:len(ciphertext)]
	
	buf = ""
	for m, k in zip(key, ciphertext):
		if type(m) is str:
			m = ord(m)
		if type(k) is str:
			k = ord(k)

		buf += chr(m^k)

	return buf


# Single byte XOR decipher
def single_xor_dec(ciphertext, key):
	plaintext = ""

	for i in range(len(ciphertext)):
		if type(ciphertext[i]) is str:
			ct = ord(ciphertext[i])
		else:
			ct = ciphertext[i]

		if type(key) is str:
			key = ord(key)
			
		plaintext += chr(ct^key)

	return plaintext


# Decrypt AES cipher in ECB mode
def aes_ecb_dec(ciphertext, key):
	cipher = AES.new(key, AES.MODE_ECB)
	return cipher.decrypt(ciphertext)

# Detect AES cipher in ECB mode
def detect_aes_ecb(ciphertext):
	return

# PKCS#7 padding 
def pkcs7_padding(block, block_size):
    return
