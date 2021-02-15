import time
import RPi.GPIO as GPIO

login_btn 		= 37
logout_btn 		= 36
arrival_btn 	= 31
departure_btn 	= 29

def log_in(name):
	if GPIO.input(login_btn) == 1:
		print(name)
		
def log_out(name):
	if GPIO.input(logout_btn) == 1:
		print(name)
		
def arrival(name):
	if GPIO.input(arrival_btn) == 1:
		print(name)
		
def departure(name):
	if GPIO.input(departure_btn) == 1:
		print(name)
		
def init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(login_btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(logout_btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(arrival_btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(departure_btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	
	GPIO.add_event_detect(login_btn, GPIO.RISING,  bouncetime=200)
	GPIO.add_event_detect(logout_btn, GPIO.RISING, bouncetime=200)
	GPIO.add_event_detect(arrival_btn, GPIO.RISING, bouncetime=200)
	GPIO.add_event_detect(departure_btn, GPIO.RISING, bouncetime=200)
	
def read(login_funcy, logout_funcy, arrival_funcy, departure_funcy, name):
	if GPIO.event_detected(login_btn):
		login_funcy(name)
		#if GPIO.input(login_btn) == 1:
		#	login_funcy(name)
		
	if GPIO.event_detected(logout_btn):
		logout_funcy(name)
		#if GPIO.input(logout_btn) == 1:
		#	logout_funcy(name)
		
	if GPIO.event_detected(arrival_btn):
		arrival_funcy(name)
		#if GPIO.input(arrival_btn) == 1:
		#	arrival_funcy(name)
		
	if GPIO.event_detected(departure_btn):
		departure_funcy(name)
		#if GPIO.input(departure_btn) == 1:
		#	departure_funcy(name)

#main()
	

