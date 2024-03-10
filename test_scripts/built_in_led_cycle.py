# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import os, machine
#os.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()

import machine
import time


led = machine.Pin(2, machine.Pin.OUT) # GPIO 2

# Main loop
while True:
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)
