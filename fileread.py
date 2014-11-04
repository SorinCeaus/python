#!/usr/bin/env python

fajl='file.py'

try:

   f=open(fajl,'r')
   sor=f.readline()
   while sor <> '':
      print sor
      sor=f.readline()
   f.close()
   print '-> file ends.'

except IOError, e:
   print 'No such file:', fajl
