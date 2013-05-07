import belaclass

str = 'bela1'
j = belaclass.Bela()
o = 'belaclass.Bela()'

try:
	k=getattr(eval(o),str,None)
	m=k()
	print 'm:', m

except TypeError, e:
	print 'TypeError: ', e
