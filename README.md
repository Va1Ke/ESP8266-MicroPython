# ESP8266 MicroPython


* Install esptool.py:
```
pip install esptool
```
* Flash ESP8266 board:
```
 esptool.py --port <Your_port> --baud 9600 write_flash --flash_size=detect 0 .\ESP8266_GENERIC-FLASH_1M-20240222-v1.22.2.bin
```
* Install Thonny IDE:
```
https://thonny.org
```
After you install Thonny, open boot.py file from the ESP8266 board using Open and write your code there.<br>
Then, press F5 and your script starts on board.

If you want to load another script, press and hold RESET button on board, plug out the board cable, wait a few seconds and plug in, then release the RESET button.<br>
Now, you can write another script and load it again using F5.