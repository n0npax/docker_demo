#!/usr/bin/env python3

from Crypto.Cipher import AES

obj = AES.new('KANGAROO', AES.MODE_CBC, 'LLAMA')
message = "Nope mate, nope"
ciphertext = obj.encrypt(message)

print(ciphertext)
