import threading
from time import sleep

class RedLight(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

        self.deactivate()

    def activate(self):
        self.activated=True

    def deactivate(self):
        self.pos=0  # number of lights on
        self.activated=False

    def get_activated(self):
        return self.activated

    def get_status(self):
        return self.pos

    def run(self):
        while True:
            if self.activated:
                i=1
                while ((i<=5) & (self.activated)):
                    self.pos=i
                    sleep(0.2)
                    i=i+1
            else:                   # añado esto para evitar que la ventana se quede
                sleep(0.2)          # "pillada" cuando las luces rojas están desactivadas