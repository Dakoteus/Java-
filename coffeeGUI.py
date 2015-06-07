from tkinter import *
import os
class Application(Frame):
    def brewit(self, pin):
        os.system("echo gpio%s > /sys/class/gpio/export  && echo high > /sys/class/gpio%s/direction && echo low > /sys/class/gpio%s/export/direction" % pin) #high, low because button

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.button1 = Button(self)
        self.button1["text"] = "Brew",
        self.button1["fg"] = "brown"
        self.button1["command"] = self.brewit

        self.button1.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
