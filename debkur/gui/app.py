#!/usr/bin/env python3
import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
import os
import getpass

class main(tk.Tk):
    def __init__(self,res="200x50",title="Debkur"):
        tk.Tk.__init__(self)
        self.geometry("{}".format(res))
        self.title("{}".format(title))
        self.entry = tk.Entry()
        self.entry.pack(fill=tk.X)
        self.button = tk.Button(self,text="Open",command=self.openfile)
        self.button.pack(side=tk.RIGHT)
        self.install = tk.Button(self,text="Install",command=self.install)
        self.install.pack(side=tk.LEFT)
        self.about = tk.Button(self,text="About",command=self.about)
        self.about.pack(side=tk.TOP)
    def openfile(self):
        file_path =tk.filedialog.askopenfilename(initialdir = "/home",title = "Select file",filetypes = (("deb files","*.deb"),("all files","*.*")))
        self.entry.insert(0,file_path)

    def install(self):
        os.system("dpkg -i {}".format(self.entry.get()))
    def about(self):
        tk.messagebox.showinfo("About", "This program was maded by ibrakap")
if __name__ == "__main__":
    if os.getuid() != 0:
        tk.messagebox.showerror("About","You must be root for run this program")
    else:    
        app = main()
        app.mainloop()

