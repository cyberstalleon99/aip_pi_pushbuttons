import time
import RPi.GPIO as GPIO

button = 37
delay = 3
debounce = .25

#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def main():

	while True:
		
		# If button is not pressed
		if GPIO.input(button) == 1:
			# Sleep for .25 seconds
			time.sleep(3)
			start_time = time.time()
			print('Button is OFF!!!')
			
			# While button is pressed down, count to 3
			counter = 0
			while GPIO.input(button) == 1:
				counter = time.time() - start_time 
				
				# Difference of delay - debounce is 2.75 but add the .25 seconds delay at the top to make it 3
				new_delay_min = delay - debounce
				new_delay_max = (delay - debounce) + .01
				
				# Execute after 3 sec  then stop after 3 sec
				if counter > new_delay_min and counter < new_delay_max:
					#pass
					print('Button is ON!!!' + str(counter))
					#break
					
			
						
		else:
			time.sleep(debounce)

def test():
	while True:
		if GPIO.input(button) == 1:
			time.sleep(3)
			print('asdf')
			
main()
#test()
		
