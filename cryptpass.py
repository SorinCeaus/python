# requires python 3
import crypt
import sys

salt=crypt.mksalt(crypt.METHOD_SHA512)
try:
        password=sys.argv[1]
except IndexError:
        print sys.argv[0],': specify a password as the first argument.'
else:
        print crypt.crypt(password, salt)
