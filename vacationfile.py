import os

maxvacationsize=1024
subject='bela subject'

try:
	f=open('vacation.txt','r')
	vacationtxt=f.read(maxvacationsize)
	f.close()
except IOError, e:
	vacationtxt='User is out of office'

msg="From,To:\nSubject:"+subject+"\n\n"+vacationtxt

print msg
