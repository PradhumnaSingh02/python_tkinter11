#hello world program in Tkinter
from tkinter import *

root = Tk()
root.title('HelloWorld')

Label(text='Hello! World', bg='red', fg= 'blue').grid(row=0, column=1)

root.mainloop()