# fun.py
# taken from learnpythonthehardway.org/book
# endless loop to display turning pipe in a cursor place
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
