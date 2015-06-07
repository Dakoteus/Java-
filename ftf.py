import time, os, curses, shutil, sys, random
import math
from termcolor import cprint
from multiprocessing import Process

class Printer:
    def print(self, text):
        print(text)

    def write(self, text):
        sys.stdout.write(text)
        sys.stdout.flush()

    def clear(self):
        os.system('clear')

class Curse:
    win = None
    y = 0
    x = 0

    def __init__(self, win):
        self.win = win

    def print(self, text, refresh=True):
        try:
            self.win.addstr(self.y, self.x, text)
        except:
            pass
        #y=min(self.win.getyx()[0] + 1, self.win.getmaxyx()[0])
        self.y += 1
        if refresh:
            self.win.refresh()

    def write(self, text, refresh=True):
        self.win.addstr(self.y, self.x, text)
        self.x += 1
        if self.x >= self.win.getmaxyx()[1]:
            self.x-=1
            self.y+=1
        if self.y >= self.win.getmaxyx()[0]:
            self.y-=1

        if refresh:
            self.win.refresh()

    def clear(self, refresh=True):
        self.win.clear()
        if refresh:
            self.win.refresh()


def frame(number, path, out=Printer()):

    file = open(path, "r")
    txt = file.read()
    lines = txt.split("\n")
    meta = lines.pop(0)
    data = meta.split(":")
    frames = int(data[1])
    frame = number%frames
    linesPerFrame = int(data[2])
    firstLine = linesPerFrame * frame
    for f in range(firstLine, firstLine+linesPerFrame):
        out.print(lines[f])


def animate(path, repeat=1, delay=None, out=Printer()):
    file = open(path, "r")
    txt = file.read()
    lines = txt.split("\n")
    meta = lines.pop(0)
    data = meta.split(":")
    delay = float(data[3]) if delay == None else delay
    frames = int(data[1])
    lpf = int(data[2])
    n = 0 if repeat == 0 else 1
    while repeat > 0 or n == 0:
        repeat -= n
        for f in range(frames):
            out.clear()
            frame(f,path,out=out)
            time.sleep(delay)


def teletype(text , speed=0.04, variation=0.02,   out=Printer()):
    for letter in text:
        out.write(letter)
        time.sleep(random.uniform(-1,1) * variation + speed)
    out.print('')


def main(stdscr):
    # Clear screen
    stdscr.clear()
    stdscr.border(0)
    stdscr.refresh()


    textBot = Curse(stdscr)
    teletype("Nothing like a cup of coffee in the morning!", out=textBot)

    
    starty=curses.LINES - 26
    startx=curses.COLS - 60

    coffeeWin = curses.newwin(26,60, starty ,startx)
    c = Curse(coffeeWin)
    coffeeGif = Process(target=animate, args=("coffee.txt",), kwargs={"repeat":0 ,"out":c})
    coffeeGif.start()
    coffeeWin.clear()
    coffeeWin.border()
    coffeeWin.addstr(0,3,"rice")
    coffeeWin.refresh()

    while(True):
        if stdscr.getkey() == "q":
            break

    #coffeeGif.terminate()
        
    
curses.wrapper(main)
