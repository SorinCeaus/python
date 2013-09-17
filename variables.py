c=10

try:
	c
	print 'c is', c
except NameError:
	print 'c is not defined.'
	c=None
	print 'c is', c

del c	# removing the variable definition
print 'c was deleted.'

try:
	c
	print 'c is', c
except NameError:
	print 'c is not defined.'
	c=None
	print 'c is', c
