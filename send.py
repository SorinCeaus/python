import smtplib
from datetime import date
from time import localtime

# get date and time
now=date.today()
mydate=now.strftime("%a, %d %b %Y")

t=localtime()
hour=t[3]
min=t[4]
sec=t[5]

rfcdate='Date: '+mydate+' '+str(hour)+':'+str(min)+':'+str(sec)

kuldo='From: qmi@localhost.localdomain.hu'
cimzett='To: teszt@localhost.localdomain.hu'
uzenet='hello haver...teszt sendmail.py'
msg=kuldo+'\n'+cimzett+'\n'+rfcdate+'\n'+uzenet
server=None


try:
	server = smtplib.SMTP('localhost')
except smtplib.socket.error, e:
	print 'Could not send mail.' % e

server.set_debuglevel(1)

if server is not None:
	try: 
		server.sendmail(kuldo,cimzett,msg)
 		server.quit()
 
 	except smtplib.SMTPSenderRefused, e:
 		print "Error happened while sending." % e
