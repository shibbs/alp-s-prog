import RPi.GPIO as GPIO
import time
import subprocess

print('Starting up spark-main')
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	pin1 = GPIO.input(18)
	pin2 = GPIO.input(19)
	if pin1 == False:
		print('Button Pressed')
		time.sleep(0.2)
		subprocess.Popen(["sudo","openocd","-f","spark-ocd.cfg"])
		print ("Done running upload cmd")
	if pin2 == False:
		print('Button2 Pressed')
		time.sleep(0.2)

