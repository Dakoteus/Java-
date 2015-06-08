import time, os, curses, shutil, sys, random
import math
from termcolor import cprint
from multiprocessing import Process
import termbox

class FTF:
    current = 0
    frames = []

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

        file = open(path, "r").read()

        lines = file.split("\n")
        meta = lines.pop(0).split(":")

        self.name = data[0].split("--")[0]
        self.frameCount = int(data[1])
        self.frameHeight = int(data[2])
        self.frameWidth = int(data[3])
        self.delay = float(data[4])

        for i in range(self.frameCount):
            frame = []
            for l in range(self.frameHeight):
                line = lines.pop(0)
                while len(line) < frameWidth:
                    line += " "

                while len(line) > frameWidth:
                    line = line[:-1]
            

    def switch(self, index):
        self.current = index
        self.out(frames[index])

    def animateYield(self,repeat=-1):
        while repeat is not 0:
            last = time.time()
            while time.time() - last < self.delay:
                yield

            switch(self.current + 1)
            
            if repeat is not -1:
                repeat -= 1;

    def animateProcess(self):
        pass

    def animate():
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

    def __init__(self, path, window, posx, posy, maxx, maxy):
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
        else if x < 0:
            self.maxx = self.window.width() + x + 1
            self.posx = self.maxx - ftf.frameWidth
        else:
            self.posx = math.floor(self.window.width()/2 - self.ftf.frameWidth/2)
            self.maxx = self.posx + self.ftf.frameWidth

        if y > 0 :
            self.posy = y - 1
            self.maxy = self.posy + self.ftf.frameHeight
        else if yx < 0:
            self.maxy = self.window.height() + y + 1
            self.posy = self.maxy - ftf.frameHeight
        else:
            self.posy = math.floor(self.window.height()/2 - self.ftf.frameHeight/2)
            self.maxy = self.posy + self.ftf.frameHeight
        
        
    def print_char(self, x, y, char, fg, bg, update=None):
        gx = x+self.posx
        gy = y+self.posy
        
        self.window.change_cell(gx, gy, char, fg, bg)

        if (update is None and self.autoRefresh_flg) or update:
            self.flush()
    
    def print_frame(self, frame,  update=None):
        for y in range(len(frame)):
            line = frame[y]
            for x in range(len(line)):
                char = line[x]
                self.print_char(x, y, char, self.window.DEFAULT, self.window.DEFAULT, update=False )
        
        if (update is None and self.autoRefresh_flg) or update:
            self.flush()

    def print_string(self, x, y, line, update=None):
        for i in range(len(line)):
            char = line[i]
            self.print_char(x+i, y, char, self.window.DEFAULT, self.window.DEFAULT, update=False )

        if (update is None and self.autoRefresh_flg) or update:
            self.flush()

    def flush(self):
        window.present()

    def set_state(self, state):
        self.ftf.switch(state)

    def clear(self, char=" "):
        for x in range(self.posx, self.maxx):
            for y in range(self.posy, self.maxy):
                self.print_char(x, y, char, self.window.DEFAULT, self.window.DEFAULT, update=False )
        
        self.flush()

termbox = Termbox()
termbox.clear()
termbox.
termbox.present()



