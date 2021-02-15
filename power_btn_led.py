import RPi.GPIO as GPIO

led = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)

if GPIO.input(led) == 1:
	GPIO.output(led, GPIO.LOW)
else:
	GPIO.output(led, GPIO.HIGH)
