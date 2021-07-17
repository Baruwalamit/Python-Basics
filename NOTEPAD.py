#this code is designed to build simple notepad using tkinter in  python

from tkinter.filedialog import *
import tkinter as tk

def savefile():
    new_file = asksaveasfile(mode='w', filetype= [('text files', '*.txt')])
    if new_file is None:
        return
    text = str(Entryfield.get(1.0, END))
    new_file.write(text)
    new_file.close()

def openfile():
    file = askopenfile(mode='r', filetype = [("text files", "*.txt")])
    if file is not None:
        content = file.read()
    Entryfield.insert(INSERT, content)

def clearfile():
    Entryfield.delete(1.0, END)


canvas= tk.Tk()
canvas.geometry("400x600")
canvas.title("Notes")
canvas.config(bg="white")
top= Frame(canvas)

top.pack(padx =10, pady =5, anchor='nw')



B1 = Button(canvas, text ="Open", bg ="white", command = openfile)
B1.pack(in_= top, side = LEFT)

B2 = Button(canvas, text = "Save", bg= "white", command = savefile)
B2.pack(in_ = top, side = LEFT)

B3 = Button (canvas, text = "Clear", bg= "white", command = clearfile)
B3.pack(in_ = top, side = LEFT)

B4 = Button(canvas, text = "Exit", bg= "white", command = exit)
B4.pack(in_ = top, side = LEFT)

Entryfield = Text(canvas, wrap= WORD, bg = "#F9DDA4", font = ("poppins",15))
Entryfield.pack(padx = 10, pady = 5, expand = TRUE , fill = BOTH)

canvas.mainloop()
