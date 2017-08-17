#!/usr/bin/env python
import RPi.GPIO as GPIO
import os
import sys
import time
import subprocess
import webbrowser
from datetime import datetime

BtnPin = 11
runGame = 1

start_time = datetime.now()
#subprocess.call(["chromium-browser", "--disable-pinch", "https://garretrcorbett.github.io/countdown_timer_application/index.html"])
webbrowser.open("https://uncw-library.github.io/escape_room_timer/index.html")

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Set BtnPin's mode is input, and pull up to high level(3.3V)
	print("setup ran")

def roomBeat(ev=None):
	global runGame
	runGame = 0
	end_time = datetime.now()
	elapsed_time = (end_time - start_time )
	url = "https://uncw-library.github.io/escape_room_timer/index.html?time={}".format(elapsed_time)
	#subprocess.call(["chromium-browser", "--kiosk", "--disable-pinch", testvar ])
	webbrowser.open(url)
	destroy()

def loop():
         
	GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=roomBeat, bouncetime=200) # wait for falling
	while runGame: 
		print("loop running")
		time.sleep(30)
			

def destroy():
	GPIO.cleanup()                     # Release resource


if __name__ == "__main__":     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
