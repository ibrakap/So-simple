import json
from tkinter import Tk, Label, Button, Entry, StringVar


class AccountGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("ArchiSteamFarmAccountGenerator")
        self.master.geometry('200x150')
        self.username = StringVar(self.master)
        self.label = Label(self.master, text="username").pack()
        self.entry = Entry(self.master, textvariable=self.username)
        self.entry.pack()
        self.label2 = Label(self.master, text="password").pack()
        self.entry2 = Entry(self.master)
        self.entry2.pack()
        self.gen = Button(self.master, text="Generate", command=self.generate_config)
        self.gen.pack()

    def generate_config(self):
        tmp = {"SteamLogin": self.entry.get() , "SteamPassword": self.entry2.get(), "Enabled": True}
        print(json.dumps(tmp, indent=2))
        with open("{}.json".format(self.entry.get()), "w") as f:
            f.write(json.dumps(tmp, indent=2))
            f.close()

if __name__ == "__main__":
    root = Tk()
    c = AccountGenerator(root)
    root.mainloop()
