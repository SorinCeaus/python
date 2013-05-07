import os
import re

def bela():
  pattern='Searching.\d.sec.\.\.\.\ndone\.'
  result = os.popen('btctl inquiry 5').read()
  matchobj = re.search(pattern,result)
  if matchobj:
  	print "talalt"
  else:
  	print "nem talalt"

def t():
	i,oe=os.popen4('btsrv -d')
	print oe.read()
	i.close()
	oe.close()

#bela()
#t()
