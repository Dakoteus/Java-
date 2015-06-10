import rpyc
import os
import time
running = False

timers=[]

brew_pin = 60

led_pins = [
    30,
    31,
    48,
    04,
    03
]

class MyService(rpyc.Service):
    def exposed_spawn_timer(seconds, seconds2):
	p = Process(target=Timer, args=(seconds,seconds2,heater_pin))
        timers.append(p)
    
    def timer(seconds, seconds2, pin):
	time.sleep(seconds)
	Myservice.on(pin)
	time.sleep(seconds2)
	MyService.off(pin)
    
    def brew_on():
    	if running is False:
            on(brew_pin)
            running = True
    
    def brew_off():
	if running is True:
            off(brew_pin)
            running = False

    def on(pin):
        os.system("echo gpio%s > /sys/class/gpio/export  && echo high > /sys/class/gpio%s/direction" % pin)
        time.sleep(200)
        os.system("echo low > /sys/class/gpio%s/direction" % pin)
    
    def off(pin):
	os.system("echo gpio%s > /sys/class/gpio/export  && echo high > /sys/class/gpio%s/direction" % pin)
        time.sleep(200)
        os.system("echo low > /sys/class/gpio%s/direction" % pin)

    def led_on():
        for pin in led_pins:
            on(pin)

    def led_off():
        for pin in led_pins:
            off(pin)

    def on_connect(self):
        # code that runs when a connection is created
        # (to init the serivce, if needed)
        pass

    def on_disconnect(self):
        # code that runs when the connection has already closed
        # (to finalize the service, if needed)
        pass

    def exposed_get_brewing(self): # this is an exposed method
        return running

    def exposed_get_state(self):
        return "running = " + str(running)

    def exposed_brew(self, boolean):
        if(boolean):
            on()
        else:
            off()


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port = 7986)
    t.start()


