import time, os, curses, shutil, sys, random
import math
from termcolor import cprint

def gif(path, delay=None):
    file = open(path, "r")
    txt = file.read()
    lines = txt.split("\n")
    meta = lines.pop(0)
    data = meta.split(":")
    delay = float(data[3]) if delay == None else delay
    frames = int(data[1])
    lpf = int(data[2])

    for f in range(frames):
        os.system('clear')
        for i in range(lpf):
            print(lines[f*lpf + i])
        time.sleep(delay)


def go(d=None):
    while True:
        gif("coffee.txt",d);

def banner(path, delay=None):
    file = open(path, "r")
    txt = file.read()
    lines = txt.split("\n")
    meta = lines.pop(0)
    data = meta.split(":")
    delay = float(data[2]) if delay == None else delay
    length = int(data[1])
    (width, height) = shutil.get_terminal_size()

    xtra = -len(lines);
    while xtra <= height:
        os.system('clear')
        for i in range(xtra if xtra > 0 else 0):
            print()
        for i in range(len(lines)):
            if i+xtra <= height and i+xtra>=0:
                cprint(lines[i],"red","on_blue", attrs=['bold'])

        xtra+=1
        time.sleep(delay)

def dgo(d=None):
    while True:
        banner("jbanner.txt",d)

def nothing(mess="    --Nothing like a cup of coffee in the morning", path="coffee.txt", delay=None):
    file = open(path, "r")
    txt = file.read()
    lines = txt.split("\n")
    meta = lines.pop(0)
    data = meta.split(":")
    delay = float(data[3]) if delay == None else delay
    frames = int(data[1])
    lpf = int(data[2])

    blah = True;
    while True:
        for f in range(frames):
            os.system('clear')
            for i in range(lpf):
                print(lines[f*lpf + i])
            if blah:
                blah=False
                teletype(mess)
            else:
                print(mess)
            time.sleep(delay)


def teletype(s):
    speed = .04 #seconds/letter
    variation = .02
        
    for l in s:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.uniform(-1,1) * variation + speed)
    print('')


# ncurses
from curses import wrapper
screen = None
def main(screen):
    screen.clear()
    screen.addstr("testing")
    screen.refresh()

wrapper(main)
