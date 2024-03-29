#!/usr/bin/python
#________________________________________
# Date created:			Thursday, 15 March 2012
#


#________________________________________
# Global imports
#

from __future__ import print_function


#________________________________________
# Class definitions
#

#
# Codex repository objects possess knowledge of enciphered codex files
#

import sys

class CodexRepository:

    def __init__(self, base_url=None):
        self.base_url		= base_url
        self.debug		= False

    def assemble_url(self, index):
        assembled_url		= '/'.join((self.base_url.rstrip('/'), str(index)))
        if self.debug:
            sys.stderr.write("[NOTICE] Assembled URL '%s'.\n" % assembled_url)
        return assembled_url

    def display(self):
        pass

#
# Cryptographic objects en{code,crypt}/de{code,crypt}
#

from base64 import b64encode, b64decode
from itertools import izip, cycle
import sys

class Crypto:

    def __init__(self, key=None, plaintext=None, ciphertext=None):
        self.ciphertext		= ciphertext
        self.debug		= False
        self.key		= key
        self.plaintext		= plaintext

    def decrypt(self):
        if self.debug:
            sys.stderr.write("[NOTICE] Performing decryption.\n")
        self.plaintext		= ''.join([chr(ord(x) ^ ord(y)) for(x,y) in izip(b64decode(self.ciphertext), cycle(self.key))])
        return self.plaintext

    def encrypt(self):
        if self.debug:
            sys.stderr.write("[NOTICE] Performing encryption.\n")
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
            sys.stderr.write("[NOTICE] Fetching URL '%s'.\n" % (self.url))
        try:
            url_handle		= urllib2.urlopen(self.url)
        except urllib2.HTTPError, e:
            if self.debug:
                sys.stderr.write("[ERROR] Received HTTP code %d, '%s', fetching URL '%s'\n" % (e.code, e.msg, self.url))
            raise e
        except urllib2.URLError, e:
            if self.debug:
                sys.stderr.write("[ERROR] '%s'\n" % (e.args))
            raise e
        content			= url_handle.read().lstrip().rstrip()
        url_handle.close()
        return content.lstrip().rstrip()

#
# This class generates mysteria for indexing the codex fragments
#

class Mysteria:

    def __init__(self):
        self.debug		= False

    #
    # Generate mysteria
    #

    def generate(self):
        pass

    def generate_primes(self):
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

    def generate_zeta(self):
        import mpmath
        import sys
        root_list		= {}
        for s in [complex(0.5,t) for t in range(10,100)]:
            try:
                root_complex	= mpmath.findroot(mpmath.zeta, s)
                if self.debug:
                    sys.stderr.write("[NOTICE] Found nontrivial zeta zero at %s.\n" % str(root_complex))
                root_imag	= float(root_complex.imag)
                try:
                    root_list[root_imag]
                    if self.debug:
                        sys.stderr.write("[NOTICE] Already found this zero, skipping.\n")
                    next
                except KeyError:
                    if root_imag > 1:
                        yield root_imag
                        root_list[root_imag] = True
                    else:
                        if self.debug:
                            sys.stderr.write("[NOTICE] Irrelevant zero, skipping.\n")
            except ValueError, e:
#DEBUG#                sys.stderr.write("Exception at s=%s: %s.\n" % (str(s), e.args[0])) #DEBUG#
                pass
            except OverflowError, e:
#DEBUG#                sys.stderr.write("Exception at s=%s: %s.\n" % (str(s), e.args[0])) #DEBUG#
                pass


#________________________________________
# Main
#

#
# Import libraries
#

import sys

#
#
#

print("""
-=| }hexdump{ CODEX RENDERER |=-


""")

print("Enter codex repository URL: ", end='')
#DEBUG#codex_repo_url			= sys.stdin.readline().lstrip().rstrip()
codex_repo_url			= 'http://maniaphobic.org/hexdump/' #DEBUG#
print("Enter decryption key: ", end='')
#DEBUG#decrypt_key			= sys.stdin.readline().lstrip().rstrip()
decrypt_key			= '$SenTieNt_ObseRver*' #DEBUG#
print()

#
# Instantiate objects:
#   - Codex repository
#   - Mysteria generator
#   - URL fetcher
#

codex_repo			= CodexRepository(codex_repo_url)
codex_repo.debug		= True #DEBUG#
mysteria			= Mysteria()
mysteria.debug			= True #DEBUG#
fetcher				= Fetcher()
fetcher.debug			= True #DEBUG#

#
# Create a list to contain the ciphertext fragments
# Iterate over the mysteria
#

ciphertext_list			= []

for mystery in mysteria.generate_zeta():
#DEBUG#    if mystery < 100: #DEBUG#
#DEBUG#        print(mystery)
#DEBUG#        continue
#DEBUG#    else:
#DEBUG#        break

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
# Instantiate a crypto object
# Assign the key
# Assemble and assign the ciphertext
# Decrypt and display the plaintext
#

crypto_obj			= Crypto()
crypto_obj.key			= decrypt_key
crypto_obj.ciphertext		= "".join(ciphertext_list)
print(crypto_obj.decrypt())

#
#
#

