#!/usr/bin/env python
#________________________________________
# Date created:			Monday, 12 March 2012
# Notes:
#     - Borrowed heavily from http://www.evanfosmark.com/2008/06/xor-encryption-with-python/
#

#
#
#

from base64 import b64encode, b64decode
from itertools import izip, cycle
import sys

#
#
#

def decrypt(key, ciphertext):
    return(''.join([chr(ord(x) ^ ord(y)) for(x,y) in izip(b64decode(ciphertext), cycle(key))]))

def encrypt(key, plaintext):
    return(b64encode(''.join([chr(ord(x) ^ ord(y)) for(x,y) in izip(plaintext, cycle(key))])))

#
#
#

key_file			= open(sys.argv[1])
key				= key_file.readlines()
key_file.close()

plaintext_file			= open(sys.argv[2])
plaintext			= plaintext_file.readlines()
plaintext_file.close()

#
#
#

print plaintext; print "\n"
ciphertext = encrypt(key, plaintext)
print ciphertext; print "\n"
plaintext = decrypt(key, ciphertext)
print plaintext


