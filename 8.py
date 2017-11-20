#!/usr/bin/env python3
#
# Challenge 8: Detect AES in ECB mode
#
from cryptopals import split_string

if __name__ == '__main__':
    with open("8.txt", 'rb') as f:
        block_size = 16
        old_uniq   = 1024 # max value 
        text = ""

        for ciphertext in f:
            uniq_blocks = set(split_string(ciphertext.strip(b'\n'), block_size))

            uniq = len(uniq_blocks)
            if uniq < old_uniq:
                text = ciphertext
                old_uniq = uniq

    print("Probably encrypted in AES ECB mode: {:}\n".format(text))
