
'''
from tkinter import *
  
class ScrollBar:
     
    # constructor
    def __init__(self):
         
        # create root window
        root = Tk()
  
        # create a horizontal scrollbar by
        # setting orient to horizontal
        h = Scrollbar(root, orient = 'horizontal')
  
        # attach Scrollbar to root window at
        # the bootom
        h.pack(side = BOTTOM, fill = X)
  
        # create a vertical scrollbar-no need
        # to write orient as it is by
        # default vertical
        v = Scrollbar(root)
  
        # attach Scrollbar to root window on
        # the side
        v.pack(side = RIGHT, fill = Y)
          
  
        # create a Text widget with 15 chars
        # width and 15 lines height
        # here xscrollcomannd is used to attach Text
        # widget to the horizontal scrollbar
        # here yscrollcomannd is used to attach Text
        # widget to the vertical scrollbar
        t = Text(root, width = 15, height = 15, wrap = NONE,
                 xscrollcommand = h.set,
                 yscrollcommand = v.set)
  
        # insert some text into the text widget
        for i in range(20):
            t.insert(END,"this is some text\n")
  
        # attach Text widget to root window at top
        t.pack(side=TOP, fill=X)
  
        # here command represents the method to
        # be executed xview is executed on
        # object 't' Here t may represent any
        # widget
        h.config(command=t.xview)
  
        # here command represents the method to
        # be executed yview is executed on
        # object 't' Here t may represent any
        # widget
        v.config(command=t.yview)
  
        # the root window handles the mouse
        # click event
        root.mainloop()
 
# create an object to Scrollbar class
s = ScrollBar()
'''
'''
from tkinter import *
tkWindow = Tk()
tkWindow.resizable(False,False)
tkWindow.title("Tkinter Scrollbar")

text = Text(tkWindow, height=8)
text.grid(row=0,column=0,)

scroll= Scrollbar(tkWindow, orient="vertical", command=text.yview)
scroll.grid(row=0,column=1,sticky="ns")
text['yscrollcommand'] = scroll.set
tkWindow.mainloop()
'''
'''
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

root = tk.Tk()

text = ScrolledText(root, width=20, height=10)
text.pack()

for i in range(30):
    cb = tk.Checkbutton(text, text=(i+1), bg='white', anchor='w')
    text.window_create('end', window=cb)
    text.insert('end', '\n')

root.mainloop()
'''
'''
import tkinter as tk

root = tk.Tk()
root.geometry("800x450")
root.title("How should i change border color")
tk.Label(root, text="How should i change border color", width=50, height=4, bg="White", highlightthickness=4, highlightbackground="#37d3ff").place(x=10, y=10)
tk.Button(root, text="Button", width=5, height=1, bg="White", highlightbackground="#37d3ff").place(x=100, y=100)


root.mainloop()
'''
'''
var_names = ["one", "two", "three"]
count = 1
for name in var_names:
    globals()[name] = count
    count += 1
    print("name :",name)
    print("count :",count)
'''
for i in range(10):
    globals() [f'x{i}'] = i
print(x2)