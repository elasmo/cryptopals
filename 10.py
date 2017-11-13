#!/usr/bin/env python3
#
# Challenge 10: Implement CBC mode
#
from cryptopals import aes_cbc_enc
from Crypto import Random

if __name__ == "__main__":
    plaintext = "blahblah"
    key = "YELLOW SUBMARINE"

    iv = Random.new().read(16) 

    print("Plaintext\t", plaintext)
    print("Key\t", key)
    print("IV\t", iv)
    print("Encrypted\t", aes_cbc_enc(plaintext, key, iv))
