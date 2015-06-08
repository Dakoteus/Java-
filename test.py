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


class Graphic:
    ftf = None

    def __init__(self, path, window):
        self.ftf = FTF(path, out=print)

box = None


try:
    box = termbox.Termbox()
    box.clear()
    box.present()

    one = Graphic("coffee.txt",box)

    two = Graphic("button.txt",box)

except:
    if box:
        box.close()

    raise

if box:
    box.close()


def tp(m):
    for x in m:
        print(x)

tp(one.ftf.frames[0])
print("\ngsadfadslkfgl;kfa;lk-----------------------------------------------------------------------------------------------------\n")
tp(two.ftf.frames[0])

