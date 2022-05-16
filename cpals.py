#!/usr/bin/env python3

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def aes_ecb_dec(ciphertext, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    plaintext = cipher.decryptor()
    return plaintext.update(ciphertext) + plaintext.finalize()

def aes_ecb_enc(plaintext, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    ciphertext = cipher.encryptor()
    return ciphertext.update(plaintext) + ciphertext.finalize()

def strxor(one, two):
    return bytes(a ^ b for (a, b) in zip(one, two))

def pkcs7_pad(block, block_size=16):
    padding_len = block_size - (len(block) % block_size)
    return block + bytes([padding_len] * padding_len)

def get_blocks(data, block_size=16):
    return [data[i:i+block_size] for i in range(0, len(data), block_size)]

def aes_cbc_enc(plaintext, key, iv, block_size=16):
    blocks = get_blocks(plaintext)
    old_block = iv
    ciphertext = b''

    for i in range(len(blocks)):
        if len(plaintext) < block_size:
            return ciphertext

        #if len(blocks[i]) < block_size:
        #    blocks[i] = pkcs7_pad(blocks[i])
        block = strxor(old_block, blocks[i])
        ciphertext += aes_ecb_enc(block, key)
        old_block = block

    return ciphertext

def aes_cbc_dec(ciphertext, key, iv, block_size=16):
    blocks = get_blocks(ciphertext)
    old_block = iv
    plaintext = b''

    for i in range(len(blocks)):
        block = blocks[i]
        plaintext_block = strxor(aes_ecb_dec(block, key), old_block)
        plaintext += plaintext_block
        old_block = block

    return plaintext
