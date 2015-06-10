import time, os, curses, shutil, sys, random
import math
from termcolor import cprint
from multiprocessing import Process
import termbox

class FTF:
    current = None
    frames = None

    path = None
    out = None

    name = None
    frameCount = None
    frameHeight = None
    frameWidth = None
    delay = None
    

    def __init__(self, path, out):
        self.path = path
        self.out = out

        doc = open(path, "r")
        file = doc.read()
        doc.close()

        lines = file.split("\n")[:]
        meta = lines.pop(0).split(":")

        self.name = meta[0].split("--")[0]
        self.frameCount = int(meta[1])
        self.frameHeight = int(meta[2])
        self.frameWidth = int(meta[3])
        self.delay = float(meta[4])

        self.current = 0
        self.frames = []
        for i in range(self.frameCount):
            frame = []
            for l in range(self.frameHeight):
                line = lines.pop(0)
                while len(line) < self.frameWidth:
                    line += " "

                while len(line) > self.frameWidth:
                    line = line[:-1]
            
                frame.append(line)
            self.frames.append(frame)

    def switch(self, index):
        if index == self.current:
            return
        self.current = index
        self.out(self.frames[index])

    def animateYield(self,repeat=-1):
        while repeat is not 0:
            last = time.time()
            while time.time() - last < self.delay:
                yield

            self.switch((self.current + 1)%self.frameCount)
           
            if repeat is not -1:
                repeat -= 1;

    def animateProcess(self):
        pass

    def animateDelay():
        pass


class Graphic:
    posx = 0
    posy = 0
    maxx = 0
    maxy = 0

    window = None
    path = None
    ftf = None

    autoRefresh_flg = True

    def __init__(self, path, window, posx=0, posy=0, maxx=0, maxy=0):
        self.posx = posx
        self.posy = posy
        self.maxx = maxx
        self.maxy = maxy
        self.window = window
        self.path = path

        self.ftf = FTF(path, out=self.print_frame)

    def resizeToFTF(self,x,y):
        if x > 0 :
            self.posx = x - 1
            self.maxx = self.posx + self.ftf.frameWidth
        elif x < 0:
            self.maxx = self.window.width() + x + 1
            self.posx = self.maxx - self.ftf.frameWidth
        else:
            self.posx = math.floor(self.window.width()/2 - self.ftf.frameWidth/2)
            self.maxx = self.posx + self.ftf.frameWidth

        if y > 0 :
            self.posy = y - 1
            self.maxy = self.posy + self.ftf.frameHeight
        elif y < 0:
            self.maxy = self.window.height() + y + 1
            self.posy = self.maxy - self.ftf.frameHeight
        else:
            self.posy = math.floor(self.window.height()/2 - self.ftf.frameHeight/2)
            self.maxy = self.posy + self.ftf.frameHeight
    def moveToLimit(self, x ,y):
        if(x>0): 
            if(self.posx<x):
                delta = x-self.posx
                self.posx+=delta
                self.maxx+=delta
        if(y>0):
            if(self.posy<y):
                delta = y-self.posy
                self.posy+=delta
                self.maxy+=delta
        if(x<0): 
            if(self.maxx>x):
                delta = x-self.posx
                self.posx+=delta
                self.maxx+=delta
        if(y<0):
            if(self.maxy>y):
                delta = self.maxy-y
                self.posy-=delta
                self.maxy-=delta
        
    def print_char(self, x, y, char, fg, bg, update=None):
        gx = x+self.posx
        gy = y+self.posy
        
        self.window.change_cell(gx, gy, ord(char), fg, bg)

        if (update is None and self.autoRefresh_flg) or update:
            self.flush()
    
    def print_frame(self, frame,  update=None):
        for y in range(len(frame)):
            line = frame[y]
            for x in range(len(line)):
                char = line[x]
                self.print_char(x, y, char, termbox.DEFAULT, termbox.DEFAULT, update=False )
        
        if (update is None and self.autoRefresh_flg) or update:
            self.flush()

    def print_string(self, x, y, line, update=None):
        for i in range(len(line)):
            char = line[i]
            self.print_char(x+i, y, char, termbox.DEFAULT, termbox.DEFAULT, update=False )

        if (update is None and self.autoRefresh_flg) or update:
            self.flush()

    def flush(self):
        self.window.present()

    def set_state(self, state):
        self.ftf.switch(state)

    def clear(self, char=" "):
        for x in range(self.posx, self.maxx):
            for y in range(self.posy, self.maxy):
                self.print_char(x, y, char, termbox.DEFAULT, termbox.DEFAULT, update=False )
        
        self.flush()

box = None




try:
    box = termbox.Termbox()
    box.clear()
    box.present()

    coffee_cup = Graphic("coffee.txt",box)
    coffee_cup.resizeToFTF(-1,-1)
    coffee_cup.set_state(0)

    button = Graphic("button.txt",box)
    button.resizeToFTF(0,0)
    #button.moveToLimit(0, -coffee_cup.posy)
    button.set_state(0)

    animation = coffee_cup.ftf.animateYield()
    button.ftf.switch(1)

    run_app = True
    while run_app:
        event = box.peek_event(timeout=30)
        if event:
            (typee, char, key, mod, width, height, mousex, mousey) = event

            if typee == termbox.EVENT_KEY and key == termbox.KEY_ESC:
                run_app = False
            if typee == termbox.EVENT_KEY and key ==termbox.KEY_ENTER:
                button.ftf.switch(1)
                time.sleep(.3)

        else:
                button.ftf.switch(0)
        next(animation)

              
except:
    if box:
        box.close()

    raise

if box:
    box.close()
