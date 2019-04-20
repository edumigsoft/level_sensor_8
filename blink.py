#
#
#
from machine import Pin
import time

class BLINK:
    
    def __init__(self, pinNum = 2, timeOn = 0.5, timeOff = 0.5):
        print("__init__")
        self.pinNum = pinNum
        self.timeOn = timeOn
        self.timeOff = timeOff
        self.pin = Pin(pinNum, Pin.OUT)
    
    def blinker(self):
        print("blinker()")
        while True:
            self.pin.off()
            print('On')
            time.sleep(self.timeOn)
            self.pin.on()
            print('Off')
            time.sleep(self.timeOff)
########################################################################

if __name__ == "__main__":
    blinker()
