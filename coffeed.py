import rpyc
import os
running = False

class MyService(rpyc.Service):
	def on(pin):
		if running is False:
			os.system("echo gpio%s > /sys/class/gpio/export  && echo high > /sys/class/gpio%s/direction && echo low > /sys/class/gpio%s/direction" % pin)
			running = True
	def off(pin):
		if running is True:
			os.system("echo gpio%s > /sys/class/gpio/export  && echo low > /sys/class/gpio%s/direction && echo high > /sys/class/gpio%s/direction" % pin)
			running = False
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
        running = boolean


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port = 7986)
    t.start()


