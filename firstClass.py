class firstClass:
	def setdata(self, value):
		self.data = value
	def display(self):
		print self.data
	
class secondClass(firstClass):
	def display(self):
		print 'mostani ertek = "%s"' % self.data
	
class thirdClass(firstClass):
	def __init__(self, value):
		self.data = value
	def __add__(self, other):
		return thirdClass(self.data + other) 	# if called, makes a new instance
	def __mul__(self, other):
		self.data = self.data * other
	
# firstClass instances
a = firstClass()
b = firstClass()
a.setdata("sztring")
b.setdata(3.14159)
a.display()
b.display()

# secondClass instances
c = secondClass()
c.setdata(42)
c.display()
a.display()

# thirdClass instances
d = thirdClass("abc")
d.display()
e = d + 'xyz'
e.display()
d * 3
d.display()
