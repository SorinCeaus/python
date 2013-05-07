#!/usr/bin/env python 
# 6-1.py - Learning Ptyhon, Ch6.1 , demonstrate operator overloading
#
class X:
	def add(self,x,y):
		print 'Not implemented yet. '
	def __add__(self,other):
		print 'here first'
		return self.add(self,other)

a = X()
a.add(1,2)
a + (1,2)

class ListAdder(X):
	def gagyi_add(self,x,y):
		return x + y
	def __init__(self, value=0):
		self.data = value
	def __add__(self,other):
		self.data = self.data + other
	def __repr__(self):
		print 'here we are'
		return `self.data`

b = ListAdder()
c = b.gagyi_add([1,2],[3,4])
print c
c = ListAdder()
c + 2
print c

class DictAdder(X):
	def add(self,d1,d2):
		r = {}
		for key in d1.keys():
			r[key] = d1[key]
		for key in d2.keys():
			r[key] = d2[key]
		return r

e = DictAdder()
print e.add({1:1},{2:2})
