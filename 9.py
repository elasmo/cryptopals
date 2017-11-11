#!/usr/bin/env python3
#
# Challenge 9: Implement PKCS #7 padding
#
from cryptopals import pkcs7_padding

if __name__ == '__main__':
    message = "YELLOW SUBMARINE"

    for block_size in range(2,20):
        padded_block = pkcs7_padding(message, block_size)
        print(block_size, padded_block,"Block length:", len(padded_block))
