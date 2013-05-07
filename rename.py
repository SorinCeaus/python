# File: rename.py
# Desc: renames files in a directory according to a given
# 	global pattern
# Date: Tue, 23 Mar 2004 17:01:03 +0200
import glob, os

DIR1="./"
DIR2="./"

os.chdir(DIR1)
for file in glob.glob('*.jpg'):
	(base, extension) = os.path.splitext(file)
	os.rename(file, os.path.join(DIR2, base + '.png'))
