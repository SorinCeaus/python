class metaClass:
	def __getattr__(self, name):	print 'get', name
	def __setattr__(self, name, value): print 'set', name, value

x = metaClass()
x.append
x.spam = "pork"
