#!/usr/bin/python
import Adafruit_BBIO.GPIO as GPIO
import time

leds = [
'/sys/class/leds/beaglebone:green:usr0/brightness',
'/sys/class/leds/beaglebone:green:usr1/brightness',
'/sys/class/leds/beaglebone:green:usr2/brightness',
'/sys/class/leds/beaglebone:green:usr3/brightness',
]

def ledon(n):
        value = open(leds[n],'w')
        value.write(str(1))
        value.close()

def ledoff(n):
        value = open(leds[n],'w')
        value.write(str(0))
        value.close()

def toggle(x):
	ledon(x)
        time.sleep(.12)
        ledoff(x)

def onDone():
	ledoff(0)
        ledoff(1)
        ledoff(2)
        ledoff(3)

import atexit
atexit.register(onDone)

while True:
	toggle(0)
        toggle(1)
        toggle(2)
        toggle(3)

