#!/usr/bin/env python
#________________________________________
#
#

#
#
#

import base64
import sys

#
#
#

try:
    operation = sys.argv[1]
except:
    operation = 'encode'

try:
    stream = open(sys.argv[2])
except:
    stream = sys.stdin

if operation == 'encode':
    function = base64.b64encode
else:
    function = base64.b64decode

print function(stream.read())







