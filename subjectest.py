sztring="Proj #:"
print 'sztring is %s' % sztring

tema="Subject: Proj #: 123-456-78"
print 'subject is %s' % tema

try:
	tema.index(sztring)
	print "sztring %s talalt" % sztring
except ValueError, e:
	print 'nem talalt', e
