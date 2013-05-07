class A:
   i = 1

   def m(self):
   	szoveg = B().m()
	return szoveg

class B:
   i = 2

   def m(self):
	szoveg = "B->m"
	return szoveg

a=A()
b=B()

print a.m()
print a.i
print b.m()
print b.i
