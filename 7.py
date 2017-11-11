#!/usr/bin/env python3
#
# Challenge 7: AES in ECB mode
#
from cryptopals import aes_ecb_dec
from base64 import b64decode

if __name__ == "__main__":
    key = "YELLOW SUBMARINE"
    f = open("7.txt", 'r')
    msg = f.read()
    f.close()
    
    print(aes_ecb_dec(b64decode(msg), key))
