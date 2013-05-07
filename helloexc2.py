# exception handling in Python language

import sys

try:
	raise TypeError, 'bela'
except TypeError, e:
	print sys.exc_type, sys.exc_value
	print "Tipushiba, %s" % e
except:
	print sys.exc_type, sys.exc_value
