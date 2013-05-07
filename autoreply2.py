#!/usr/bin/env python
#
# File: autoreply.py
# Desc: autoreply script
# Version: 0.2.0
# Author: Miklos Quartus <qmi@libren.hu> - Libren Ltd., HUNGARY
import os
import sys
import smtplib

maxvacationsize=1024
server = None
recipient = sys.argv[1]
sender = sys.argv[2] 
subject = "Out of Office Autoreply"

try:
	f=open('/etc/postfix/vacation.txt','r')
	vacationtxt=f.read(maxvacationsize)
	f.close()
except IOError, e:
	vacationtxt="I'm afraid that "+sender+" is out of office."

msg="From: "+sender+"\nTo: "+recipient+"\nSubject: "+subject+"\n\n"+vacationtxt

server = smtplib.SMTP('localhost')
if server is not None:

	try: 
		server.sendmail(sender,recipient,msg)
		server.quit()
	except smtplib.SMTPSenderRefused, e:
		print "Error happened" % e
