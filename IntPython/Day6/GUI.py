#Example (Hello, World):

import tkinter
from tkinter.constants import *
tk = tkinter.Tk()
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=10)
frame.pack(fill=BOTH,expand=1)
label = tkinter.Label(frame, text="Hello, John")
label.pack(fill=X, expand=1)
button = tkinter.Button(frame,text="Exit",command=tk.destroy)
button.pack(side=TOP)
tk.mainloop()