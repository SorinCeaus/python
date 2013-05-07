# -*- coding: iso-8859-2 -*-
# Kilistazza a tiz percnel vagy regebben futo progikat
# Szerzo: Quartus Miklós
# Dátum: Wed Nov 10 17:42:46 CET 2004

import os

a=os.system("ps ax | awk -F' ' '{print $1,$4}' > /tmp/pidtime ")
if a != 0: print 'a nem null: ', a

print 'feldolgozas...'
f=open('/tmp/pidtime', 'r')
print 'PID TIME'
line=f.readline()
line=f.readline()
while line != '':
	index=line.find(':')
	if index==-1: break
	perc=line[index+1:]
	ora=line[index-2:index]
	p=int(perc)
	o=int(ora)
	if ((p >= 10) or (o > 0)):
		print line, 
	else:
		pass
	line=f.readline()
print 'kesz.'
f.close()
