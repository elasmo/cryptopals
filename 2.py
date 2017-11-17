#!/usr/bin/env python3
#
# Challenge 2: Fixed XOR
#
from cryptopals import hexstr_xor

if __name__ == "__main__":
    buf1 = "1c0111001f010100061a024b53535009181c"
    buf2 = "686974207468652062756c6c277320657965"

    print(hexstr_xor(buf1, buf2))
