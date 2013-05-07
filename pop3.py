import poplib

pophost='localhost'
user='teszt'
pw='teszt12'

p = poplib.POP3(pophost)
p.user(user)
p.pass_(pw)
msg = p.retr(1)
print msg
p.quit()
