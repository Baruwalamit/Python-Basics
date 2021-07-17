#this code is to build a simple working clock using tkiner in python

from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()

root.title("Clock")
def show_time():
    string = strftime("%I:%M:%S %p")
    label.config(text = string)
    label.after(1000, show_time)

label = Label (root, font=("ds-digital",80), background ="black", foreground ="cyan")
label.pack(anchor ="center", expand = True)
show_time()
root.mainloop()
