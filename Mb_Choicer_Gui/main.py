#!/usr/bin/python3
import tkinter as tk
import tkinter.messagebox
import os
__author__="ibrakap"
__version__ = "1.0"
__email__ = "ibrakap@gmail.com"
__bannerlord_status__ = "Waiting"
"""
I don't use python open function(like fopen()) because give me was error and slow.
"""
class main(tk.Tk):
    def __init__(self,resolution="300x200",title="Mb Choicer"):
        tk.Tk.__init__(self)
        self.geometry("{}".format(resolution))
        self.title("{}".format(title))
        self.button = tk.Button(self,text="Native(Pure)",command=self.playnative)
        self.button.pack()
        self.button1 = tk.Button(self,text="Viking Conquest",command=self.playviking)
        self.button1.pack()
        self.button2 = tk.Button(self,text="Napoleonic Wars",command=self.playnapolion)
        self.button2.pack()
        self.text = tk.Label(self,text="Or any mod(Write mod folder name)")
        self.text.pack()
        self.entry = tk.Entry(self)
        self.entry.pack()
        self.button3 = tk.Button(self,text="Play mod",command=self.playmod)
        self.button3.pack()
        self.button4 = tk.Button(self,text="About",command=self.info)
        self.button4.pack(side=tk.LEFT)
        self.button5 = tk.Button(self,text="Exit",command=self.exit)
        self.button5.pack(side=tk.RIGHT)
    def playnative(self):
        os.system("""echo "Native" > /home/$USER/.mbwarband/last_module_warband""")
        os.system("""/home/$USER/.steam/steam/steamapps/common/MountBlade\ Warband/./mb_warband.sh""")
    def playviking(self):
        os.system("""echo "Viking Conquest" > /home/$USER/.mbwarband/last_module_warband""")
        os.system("/home/$USER/.steam/steam/steamapps/common/MountBlade\ Warband/./mb_warband.sh")
    def playnapolion(self):
        os.system("""echo "Napoleonic Wars" > /home/$USER/.mbwarband/last_module_warband""")
        os.system("/home/$USER/.steam/steam/steamapps/common/MountBlade\ Warband/./mb_warband.sh")
    def playmod(self):
        os.system("""echo "{}" > /home/$USER/.mbwarband/last_module_warband""".format(self.entry.get()))
        os.system("""/home/$USER/.steam/steam/steamapps/common/MountBlade\ Warband/./mb_warband.sh""")
    def exit(self):
        exit()
    def info(self):
        tk.messagebox.showinfo("About","""This program was maked by ibrakap
for Mount And Blade Warband. For Linux and Mac os(Mac os not tested).""")
if __name__ == "__main__":
    app = main()
    app.resizable(True,False)
    app.mainloop()
