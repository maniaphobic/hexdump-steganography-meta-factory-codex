#!/usr/bin/python
#________________________________________
# Date created:			Thursday, 15 March 2012
#

#________________________________________
# Global imports
#

import sys


#________________________________________
# Class definitions
#

#
# 
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
            print("[ERROR] Received HTTP code %d, '%s', fetching URL '%s'" % (e.code, e.msg, self.url))
            exit(1)
        except urllib2.URLError, e:
            print("[ERROR] '%s'" % (e.args))
            exit(1)
        content			= url_handle.read().lstrip().rstrip()
        url_handle.close()
        return content

#
# 
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
# 
#

class Mysteria:

    def __init__(self):
        pass

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
#
#

try:
    key				= sys.argv[1]
except:
    key				= "I want to believe."

#
#
#

base_url			= "http://maniaphobic.org/hexdump"
mysteria			= Mysteria()
ciphertext_list			= []

fetcher				= Fetcher()
fetcher.debug			= True
for value in mysteria.generate():
    fetcher.url			= "%s/%s.txt" % (base_url, str(value))
    try:
        ciphertext_list.append(fetcher.fetch().lstrip().rstrip())
    except:
        break

#
#
#

crypto_obj			= Crypto()
crypto_obj.key			= key
crypto_obj.ciphertext		= "".join(ciphertext_list)
print(crypto_obj.decrypt())

#
#
#

