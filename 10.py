#!/usr/bin/env python3
#
# Challenge 10: Implement CBC mode
#
from cryptopals import aes_cbc_enc

if __name__ == "__main__":
    plaintext = "blahblah"
    key = "YELLOW SUBMARINE"

    aes_cbc_enc(plaintext, key)
