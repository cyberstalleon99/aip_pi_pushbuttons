# This script is being run at startup and shutdown
# Copy of this script is the one being executed at /lib/systemd/system-shutdown
import RPi.GPIO as GPIO

led = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)

if GPIO.input(led) == 1:
	GPIO.output(led, GPIO.LOW)
else:
	GPIO.output(led, GPIO.HIGH)
