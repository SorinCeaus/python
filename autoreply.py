#!/usr/bin/env python
#
# File: autoreply.py
# Desc: autoreply script
# Author: Miklos Quartus <qmi@libren.hu> - Libren Ltd., HUNGARY

import sys
import os
import smtplib

server = None
recipient = sys.argv[1]
sender = sys.argv[2] 
subject = "Out of Office Autoreply"
msg = "\
From: "+sender+"\n\
To: "+recipient+"\n\
Subject: "+subject+"\n\
Thank-you for your email...\n\n\
I will be on annual leave from Monday 23rd May, returning to the office on Tuesday 14th June.\n\
If you could please forward your enquiries to the following people it would be greatly appreciated:\n\n\n\
Russell Athletic/Sherrin/Spalding\n\
Customer Service\n\
Ph:  03 9765 5999\n\n\n\
Edge Marketing\n\
General Enquiries\n\
Ph:  07 3891 9991\n\n\n\
Alternatively, I look forward to responding to your message upon \
my return.\n\n\
Kind Regards,\n\n\
Rani..."

server = smtplib.SMTP('localhost')
if server is not None:

	try: 
		server.sendmail(sender,recipient,msg)
		server.quit()
	except smtplib.SMTPSenderRefused, e:
		print "Error happened" % e
