import time
import RPi.GPIO as GPIO

# ===========================================================================
# =============================For Long Press==============================

#delay = 3
#debounce = .25

def longpress():
	counter = 0
	while True:
		
		# If button is not pressed
		if GPIO.input(button) == 1:
			# Sleep for .25 seconds
			time.sleep(.25)
			start_time = time.time()
			print('asdfsdf')
			# While button is pressed down, count to 3
			
			while GPIO.input(button) == 1:
				counter = time.time() - start_time 
				#print(counter)
				# Difference of delay - debounce is 2.75 but add the .25 seconds delay at the top to make it 3
				new_delay_min = delay - debounce
				new_delay_max = (delay - debounce) + .01
				print('asdfffffff')
				
				# Execute after 3 sec  then stop after 3 sec
				if counter > new_delay_min and counter < new_delay_max:
					print('Button is ON!!!' + str(counter))
					#break
			
			if counter < 1:
				print('Counter: ' + str(counter))
				#rint('Single Press')
		
		else:
			time.sleep(debounce)

test_counter = 0			
def test1(txt):
	global test_counter
	counter = 0

	time.sleep(.25)
	start_time = time.time()
	
	while GPIO.input(button) == 1:
		
		counter = time.time() - start_time
		new_delay_min = delay - debounce
		new_delay_max = (delay - debounce) + .01
		#print(counter)
		if counter > new_delay_min and counter < new_delay_max:
			print('Button is ON!!!' + str(counter))
			break

# ===========================================================================
		
		
