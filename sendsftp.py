#!/usr/bin/python
# sendsftp.py
# sends file over sftp interactively to atpco ftp server
# by miklos quartus (c) 2013 flybe

import pexpect
import sys

#filename='BE_TEST.DAT'
if len(sys.argv) < 2:
        print "Usage: sendsftp.py <filename>"
        sys.exit("No filename was specified.")
else:
        filename=str(sys.argv[1])

#print filename
child = pexpect.spawn('sftp XBE0FT2@ftpin.atpco.net')
child.expect('XBE0FT2@ftpin.atpco.net.s password:.')
child.sendline('XXXXXX')
child.expect('sftp>.')
# the below mode is to be used only for TEXT files!
child.sendline('ls /+mode=text,lrecl=160,recfm=fb,blksize=0')
child.expect('sftp>.')
sendparam='put '+filename+' //!XBE.PROD.XMTBERCN.IDECP'
child.sendline(sendparam)
child.expect('sftp>.')
child.sendline('quit')
print child.before
