# Function argument types
def f2(a, *b): print a,b 	# positional varargs
def f3(a, **b): print a,b	# keyword varargs
def f4(a, *b, **c): print a,b,c	# mixed modes
def f5(a, b=2, c=3): print a,b,c	# defaults

f2(1,2)
f3(1)
f4(1,2,3)
f5(1,4)
