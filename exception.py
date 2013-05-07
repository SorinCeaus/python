# exception handling in Python language

myException = 'Error'

def raiser1():
	raise myException, "hello" 	# force an exception

def raiser2():
	raise myException	# force an exception

def tryer(func):
	try:
		func()
	except myException, extraInfo:
		print 'got this:', extraInfo

tryer(raiser1)
tryer(raiser2)
