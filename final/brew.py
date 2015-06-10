#! /usr/bin/python

import rpyc
import sys, time, random
from optparse import OptionParser


def teletype(s):
    speed = .04 #seconds/letter
    variation = .02
        
    for l in s:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.uniform(-1,1) * variation + speed)
    print('')

parser = OptionParser()

parser.add_option("-t", "--target", dest="target", default="localhost", help="the target ip/url for the server")
parser.add_option("-p", "--port", dest="port", type="int", default=7986, help="the port on which the coffee server is running")

parser.add_option("--off", action="store_const", const="stop", dest="set_state", help="stop making coffee")
parser.add_option("--on", action="store_const", const="start", dest="set_state", help="start maiing coffee")
parser.add_option("--toggle", action="store_const", const="toggle", dest="set_state", help="toggle coffemaker state")
parser.set_defaults(set_state="none")

parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=True, help="print coffee maker state")
parser.add_option("-q", "--quiet", action="store_false", dest="verbose", help="don't output state information")

parser.add_option("-s", "--status", action="store_true", dest="get_state", default=False, help="get status of the coffemaker")

(options, args) = parser.parse_args()

daemon = rpyc.connect(options.target, options.port);
service = daemon.root


if options.set_state is not "none":
    on = None

    if options.set_state == "start":
        on = True
    if options.set_state == "stop":
        on = False
    if options.set_state == "toggle":
        on = not service.get_brewing()

    service.brew(on)
   
    state = service.get_state()
    print(state)

elif options.get_state:
    state = service.get_state()
    print(state)

else:
#elif len(sys.argv) < 2:
    teletype("Nothing like the smell of coffee in the morning!")
    exit()
