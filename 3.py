#!/usr/bin/env python3
#
# Challenge 3: Single-byte XOR cipher
#
import binascii
from string import ascii_letters
from cryptopals import single_key_xor
from cryptopals import count_chars
from cryptopals import calc_score

cipherstr = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
ciphertext = binascii.unhexlify(cipherstr)

score = 0
old_score = 0

# Try decrypt cipher text using keys A-Aa-z and store in list
for key in ascii_letters:
    deciphered = single_key_xor(ciphertext, key)
    freqs = count_chars(deciphered)
    score = calc_score(freqs)

    if score > old_score:
        plaintext = deciphered
        old_score = score
    
print("Possibly deciphered text: '" + plaintext + "'")
