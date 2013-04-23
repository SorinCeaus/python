#!/usr/bin/env python
# taken somewhere from the internet
# passwordgenerator.py
import string
from random import choice
 
size = 8
password=''.join([choice(string.letters + string.digits) for i in range(size)])
print password
