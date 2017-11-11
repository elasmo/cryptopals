#!/usr/bin/env python3
#
# Challenge 9: Implement PKCS #7 padding
#
from cryptopals import pkcs7_padding

if __name__ == '__main__':
    message = "YELLOW SUBMARINE"
    block_size = 20

    print(pkcs7_padding(message, block_size))
