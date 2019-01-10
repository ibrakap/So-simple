#!/usr/bin/python3
from tkinter import *
from tkinter import messagebox
import webbrowser as web
top = Tk()
top.title("Clik me!")
top.geometry("200x200")
lbl = Label(text = "Clik me!")
lbl.pack()
def Hello():
 msg = messagebox.showinfo( "Clik me!", "Hello")
 print("User clickced")
B = Button(top, text = "Clik me!", command = Hello)
B.place(x = 50,y = 50)

def Link():
    link = web.open("https://github.com/ibrakap")
but = Button(top, text = "Visit us", command = Link)
but.place(x = 125, y = 170)

def exitt():
 print("User exit")
 exit()
ab = Button(top, text = "Exit",command = exitt)
ab.place(x = 80,y = 80)
top.mainloop()
