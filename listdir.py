import os

projectdir="/home/pcguest/DOCUMENTS"

r=os.access(projectdir,os.R_OK)
if r: 
	print '%s is readable.' % projectdir
else:
	print '%s is not readable.' % projectdir

l=os.listdir(projectdir)
for dir in l:
	print dir
