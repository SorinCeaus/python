# CAE Engineering - szakmai teszt
# Tue Nov  4 20:17:27 CET 2014
# They wanted me to use an weird scripting language 'nasal' to solve it.
# Here is it in Python :)
# Adding 100 random elements of numbers to an array (list)
# Calculate an average of the numbers in the array 

import random

#### fill array with 100 random numbers between
a=[]
i=0
print "Adding random elements to array."
for i in range(0,100):
	a.append(random.randint(1,100))
	print "Random element in array: %d" % a[i]
print "%d of elements to array added." % len(a)

#### calculate average
average=0
for i in a:
	average=average+i

result=average/100
print "Average is: %d" % result
