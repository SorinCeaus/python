#!/usr/bin/env python2.4
#
# File: feedheader.py

senderisfound=0

header = ['bela', 'Date: Tue, 11 Oct', 'From: \"Miklos Quartus\" <qmi@localhost.localdomain.hu>']
for i, v in enumerate(header):
	if v.find("From:") is 0:
		print 'sender found'
		print v
		senderisfound=1
		break

if senderisfound is not 1:
	print 'sender not found'
