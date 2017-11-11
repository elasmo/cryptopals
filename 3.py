#!/usr/bin/env python3
#
# Challenge 3: Single-byte XOR cipher
#
import binascii
from string import ascii_letters
from string import ascii_lowercase
from cryptopals import single_key_xor

cipherstr = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
ciphertext = binascii.unhexlify(cipherstr)

freq_en = { 
    'a' : 8.167, 'b' : 1.492, 'c' : 2.782, 'd' : 4.253, 'e' : 12.702,
    'f' : 2.228, 'g' : 2.015, 'h' : 6.094, 'i' : 6.966, 'j' : 0.153, 
    'k' : 0.772, 'l' : 4.025, 'm' : 2.406, 'n' : 6.749, 'o' : 7.507, 
    'p' : 1.929, 'q' : 0.095, 'r' : 5.987, 's' : 6.327, 't' : 9.056, 
    'u' : 2.758, 'v' : 0.978, 'w' : 2.360, 'x' : 0.150, 'y' : 1.974, 
    'z' : 0.074
}

plaintext = ""
buffers = []
freqs = {}
score = {}

# Try decrypt cipher text using keys A-Aa-z and store in list
for key in ascii_letters:
	buffers.append(single_key_xor(ciphertext, key))

# Count characters
for buf in buffers:
    freqs[buf] = dict.fromkeys(ascii_lowercase, 0)

    for char in buf:
        val = ord(char)
        if val >= ord('a') and val <= ord('z'):
            freqs[buf][char] += 1
            
# Analyze
n_buf = 0
for buf in buffers:
    score[buf] = 0;

    for letter, occurance in freqs[buf].items():
        letter_freq = occurance/len(buf)
        score[buf] += freq_en[letter]+letter_freq

    n_buf += 1

# Rank
n_score = 0
highest_score = ""
for k, v in score.items():
    if v > n_score:
        highest_score = k
        n_score = v

print("Possibly deciphered text: '" + highest_score + "'")
