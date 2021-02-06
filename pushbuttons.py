import RPi.GPIO as GPIO

login_btn = 37
logout_btn = 36

def init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(login_btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(logout_btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.add_event_detect(login_btn, GPIO.FALLING, bouncetime=200)
	GPIO.add_event_detect(logout_btn, GPIO.FALLING, bouncetime=200)
	
def read(log_in_func, log_out_func, name):
	if GPIO.event_detected(login_btn):
		log_in_func(name)
		
	if GPIO.event_detected(logout_btn):
		log_out_func(name)

