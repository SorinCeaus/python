import os
import re

pipe = os.popen('pidof btsrv')  # is btsrv running?
result = pipe.read()
result = re.sub("\n","",result) # strip newline char
pattern = "\d"                  # any decimal digit (like [0-9])
if not re.search(pattern,result):
	print "btsrv is not running, exiting."
else:
     print "btsrv is running (PID "+result+")"
