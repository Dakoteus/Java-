import rpyc
import os
import time
6

class MyService(rpyc.Service):
    running = False

    timers=[]   

    brew_pin = 60

    led_pins = [30, 31, 48, 4, 3 ]
    led_go = True

    coffee_port = 7986

    def exposed_spawn_timer(self, seconds, seconds2):
        p = Process(target=self.timer, args=(seconds,seconds2,self.brew_pin))
        self.timers.append(p)
    
    def timer(self, seconds, seconds2, pin):
        time.sleep(seconds)
        self.brew_on(pin)
        time.sleep(seconds2)
        self.brew_off(pin)
    
    def brew_on(self):
        if self.running is False:
            self.on(self.brew_pin)
            self.running = True
    
    def brew_off(self):
        if self.running is True:
            self.off(self.brew_pin)
            self.running = False

    def on(self, pin):
        os.system("echo gpio%s > /sys/class/gpio/export  && echo high > /sys/class/gpio%s/direction" % pin)
        time.sleep(.2)
        os.system("echo low > /sys/class/gpio%s/direction" % pin)
    
    def off(self, pin):
        os.system("echo gpio%s > /sys/class/gpio/export  && echo high > /sys/class/gpio%s/direction" % pin)
        time.sleep(.2)
        os.system("echo low > /sys/class/gpio%s/direction" % pin)

    def led_on(self):
        for pin in self.led_pins:
            self.on(pin)

    def led_off(self):
        for pin in self.led_pins:
            self.off(pin)

    def led_flash(delay):
        self.led_go = True
        while self.led_go:
            self.led_on()
            time.sleep(delay)
            self.led_off()
            time.sleep(delay)

    def on_connect(self):
        # code that runs when a connection is created
        # (to init the serivce, if needed)
        pass

    def on_disconnect(self):
        # code that runs when the connection has already closed
        # (to finalize the service, if needed)
        pass

    def exposed_get_brewing(self): # this is an exposed method
        return self.running

    def exposed_get_state(self):
        return "running = " + str(self.running)

    def exposed_brew(self, boolean):
        if(boolean):
            self.brew_on()
        else:
            self.brew_off()

    def exposed_led_test(self):
        self.led_on()
        time.sleep(1)
        self.led_off()

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port = coffee_port)
    t.start()


