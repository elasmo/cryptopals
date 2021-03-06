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

# Letter frequency analysis. Score is based on a english reference added with
# the current letter frequency.
def calc_score(freqs):
    score = 0
    for char, occur in freqs.items():
    	score += freq_en[char] + occur

    return score

# Count lowercase ascii letters in a string
def count_chars(text):
    freqs = dict.fromkeys(ascii_lowercase, 0)
    freqs.update({' ' : 0})
    
    for char in text.lower():
        val = ord(char)
        if val >= ord('a') and val <= ord('z') or val == ord(' '):
            freqs[char] += 1
            
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
	# Compare the first block of n bytes with the following blocks and
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

# Calculate hamming distance between two strings of equal length
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

# Take two equal length buffers and produce their XOR combination
def hexstr_xor(str1, str2):
    if len(str1) != len(str2):
    	raise ValueError("Strings not of equal length")

    hex_one = binascii.unhexlify(str1)
    hex_two = binascii.unhexlify(str2)

    result = ""
    for val1, val2 in zip(hex_one, hex_two):
        result += chr(val1^val2)

    # str.encode returns a utf-8 encoded (default) bytes object
    return binascii.hexlify(str.encode(result))

# Split a string into blocks
def split_string(text, block_size):
    return [text[i:i+block_size] for i in range(0, len(text), block_size)]

# Transpose blocks: make a block that is the first byte of every block, 
# and a block that is the second byte of every block, and so on. 
def transp_blocks(blocks):
    transp_list = []

    keylen = len(blocks[0])
    for char in range(keylen):
        buf = bytes()

        for block in blocks:
            buf += block[char:char+1]

        transp_list.append(buf)

    return transp_list

# Repeating-XOR decipher
def repeating_key_xor(ciphertext, key):
    if len(ciphertext) != len(key):
    	# XXX: should I use padding instead(?)
    	key = key[0:len(ciphertext)]
	
    buf = ""
    for char, key in zip(key, ciphertext):
        if type(char) is str:
            char = ord(char)
        if type(key) is str:
            key = ord(key)

        buf += chr(char^key)

    return buf

# Single key XOR
def single_key_xor(ciphertext, key):
    plaintext = ""
    
    for char in ciphertext:
        if type(char) is str:
            char = ord(char)
        else:
            char = char

        if type(key) is str:
            key = ord(key)

        plaintext += chr(char^key)
    
    return plaintext

# Encrypt with AES in CBC mode
def aes_cbc_enc(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = pkcs7_padding(plaintext, AES.block_size)

    result = b""
    # XXX: broken
    for i, p in zip(iv, plaintext):
        result += str.encode(chr(i^p), 'iso-8859-1')

    return cipher.encrypt(result)

# Decrypt AES cipher in ECB mode
def aes_ecb_dec(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(ciphertext)

# PKCS#7 padding 
def pkcs7_padding(block, block_size):
    padding_len = block_size - (len(block) % block_size)

    if block is str:
        block = str.encode(block)

    for p in range(padding_len):
        block += bytes(chr(padding_len), 'utf-8')

    return block
