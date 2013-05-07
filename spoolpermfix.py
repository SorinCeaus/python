#!/usr/bin/env python
# Author: qmi <qmi@libren.hu>

import os
fajl='/etc/virtual/domainowners'

print 'spool dir perm fix...'

try:

   f=open(fajl,'r')
   sor=f.readline()
   while sor <> '':
	 kpindex=sor.find(':')
	 domain=sor[:kpindex]
	 owner=sor[kpindex+1:]
	 sowner=owner.strip()
	 parancs="chown -R "+sowner+" /var/spool/virtual/"+domain
	 os.system(parancs)
	 #print parancs
	 sor=f.readline()
   f.close()
   print '-> fajl vege.'

except IOError, e:
   print 'Nincs ilyen fajl:', fajl

print 'kesz.'
