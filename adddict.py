# function merging two dictionaries
def adddict(a,b):
	new = {}
	for key in a.keys():
		new[key] = a[key]
	for key in b.keys():
		new[key] = b[key]
	return new

# main
e = {1:1,2:2}
print e
f = {3:3,4:4}
print f 
print adddict(e,f)
