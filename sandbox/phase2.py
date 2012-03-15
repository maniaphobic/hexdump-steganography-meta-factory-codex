#!/usr/bin/python
#________________________________________
# Date created:			Thursday, 15 March 2012
#


#________________________________________
# Class definitions
#

#
# Codex repository objects possess knowledge of enciphered codex files
#

class CodexRepository:

    def __init__(self, base_url=None, cell=None):
        self.base_url		= base_url
        self.cell		= cell

    def assemble_url(self, arg):
        return "%s/%s/%s" % (self.base_url, self.cell, str(arg))

#
# Cryptographic objects en{code,crypt}/de{code,crypt}
#

from base64 import b64encode, b64decode
from itertools import izip, cycle

class Crypto:

    def __init__(self, key=None, plaintext=None, ciphertext=None):
        self.ciphertext		= ciphertext
        self.debug		= False
        self.key		= key
        self.plaintext		= plaintext

    def decrypt(self):
        self.plaintext		= ''.join([chr(ord(x) ^ ord(y)) for(x,y) in izip(b64decode(self.ciphertext), cycle(self.key))])
        return self.plaintext

    def encrypt(self):
        self.ciphertext		= b64encode(''.join([chr(ord(x) ^ ord(y)) for(x,y) in izip(self.plaintext, cycle(self.key))]))
        return self.ciphertext

#
# The utility class fetches URLs
#

import sys
import urllib2

class Fetcher:

    def __init__(self, url=None):
        self.debug		= False
        self.url		= url

    def fetch(self):
        if self.debug:
            sys.stderr.write("[DEBUG] Fetching URL '%s'.\n" % (self.url))
        try:
            url_handle		= urllib2.urlopen(self.url)
        except urllib2.HTTPError, e:
            sys.stderr.write("[ERROR] Received HTTP code %d, '%s', fetching URL '%s'" % (e.code, e.msg, self.url))
            exit(1)
        except urllib2.URLError, e:
            sys.stderr.write("[ERROR] '%s'" % (e.args))
            exit(1)
        content			= url_handle.read().lstrip().rstrip()
        url_handle.close()
        return content.lstrip().rstrip()

#
# This class generates mysteria for indexing the codex fragments
#

class Mysteria:

    def __init__(self):
        pass

    #
    # Generate mysteria
    #

    def generate(self):
        prime_list		= [2]
        yield prime_list[0]
        i			= 3
        while True:
            is_prime		= True
            for prime in prime_list:
                if i%prime == 0:
                    is_prime	= False
                    break
            if is_prime:
                yield i
                prime_list.append(i)
            i			+= 2


#________________________________________
# Main
#

#
# Import libraries
#

import sys

#
# Instantiate objects:
#   - Codex repository
#   - Mysteria generator
#   - URL fetcher
#

codex_repo			= CodexRepository('http://maniaphobic.org', 'hexdump')
mysteria			= Mysteria()
fetcher				= Fetcher()

#
# Create a list to contain the ciphertext fragments
# Iterate over the mysteria
#

ciphertext_list			= []

for mystery in mysteria.generate():

    #
    # Assemble the codex URL
    # Attempt to fetch the URL, appending to the ciphertext list if successful
    # Exit the loop upon error
    #

    fetcher.url			= codex_repo.assemble_url(mystery)
    try:
        ciphertext_list.append(fetcher.fetch())
    except:
        break

#
# Import the cryptographic key from the command line
# Instantiate a crypto object
# Assign the key
# Assemble and assign the ciphertext
# Decrypt and display the plaintext
#

try:
    key				= sys.argv[1]
except:
    key				= "I want to believe."
crypto_obj			= Crypto()
crypto_obj.key			= key
crypto_obj.ciphertext		= "".join(ciphertext_list)
print(crypto_obj.decrypt())

#
#
#

