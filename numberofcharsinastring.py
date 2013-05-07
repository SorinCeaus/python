#!/usr/bin/python
# count a number of characters in a string
# Copyright (C) 2013 Miklos Quartus - Tue Jan 15 00:02:26 GMT 2013

a="asdf,asdfas,,asdf,,,234234,23425,,,,,,,,,,,,,,,,,,,,,,,,,,,,"
print "string --->", a
nofcommas=a.count(",")
print "the number of commas --->", nofcommas
