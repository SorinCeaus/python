import random
from Tkinter import *

root = Tk()

eredmeny=random.randint(1,20)

w = Label(root, text=str(eredmeny), font=100)
w.pack()

root.mainloop()
