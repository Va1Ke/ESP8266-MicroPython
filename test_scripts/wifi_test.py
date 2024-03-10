# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import os, machine
#os.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()
import network
import urequests

ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
    
sta_if.connect('WIFI_name', 'WIFI_password')

api_url = "http://jsonplaceholder.typicode.com/todos/1"
response = urequests.get(api_url)
print(response.json())