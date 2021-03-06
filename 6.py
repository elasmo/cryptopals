#!/usr/bin/env python3
#
# Challenge 6: Break repeating-key XOR ("Vigenére")
# 

from cryptopals import *
from base64 import b64decode

with open("6.txt", "rb") as f:
    data = f.read()

ciphertext = b64decode(data)

print("Ciphertext:", ciphertext)

if __name__ == "__main__":
    # Guess key length
    guessed_keylen = guess_keylen(ciphertext, minlen=2, maxlen=40)
    print("Guessed key length:", guessed_keylen)

    # Split ciphertext in keylen n byte blocks and transpose 
    ciphertext_blocks = split_string(ciphertext, guessed_keylen)
    ciphertext_transp = transp_blocks(ciphertext_blocks)

    # Decrypt transposed ciphertext blocks using ascii [0-254] as key
    # ..and try finding the key that harvest the best scores
    guessed_key = ""

    for block in ciphertext_transp:
        score = old_score = 0
        key_part = ""

        for key in range(255):
            plaintext = single_key_xor(block, key)

            freq  = count_chars(plaintext)
            score = calc_score(freq)

            if(score > old_score):
                old_score = score
                key_part = chr(key)

        guessed_key = ''.join([guessed_key, key_part])

    print("Encryption key: " + guessed_key)

    # Finally!
    deciphered = ""
    for block in ciphertext_blocks:
        deciphered = ''.join([deciphered, repeating_key_xor(block, guessed_key)])

    print("Dechiphered:\n" + deciphered)
