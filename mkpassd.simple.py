import crypt
import sys
salt=crypt.mksalt(crypt.METHOD_SHA512)
password=sys.argv[1]
print crypt.crypt(password, salt)
