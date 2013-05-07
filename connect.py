#/usr/bin/env python

import MySQLdb

db=MySQLdb.connect(user="qmi",passwd="",db="telehaz")
c=db.cursor()

try:
	c.execute("select * from telehazhasznalat")
	r=c.fetchall()
	#r=c.fetchone()

except MySQLdb.ProgrammingError, e:
	print e
	r='hiba'

print r
c.close()
db.close()
