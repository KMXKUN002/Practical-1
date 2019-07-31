#!/usr/bin/python3
"""
Names: <Chris Kim>
Student Number: <KMXKUN002>
Prac: <1>
Date: <26/07/2019>
"""

# import Relevant Librares
import RPi.GPIO as GPIO

# Set GPIO mode to BOARD
GPIO.setmode (GPIO.BOARD)
GPIO.setwarnings (False)

# Create global counter
count = 0

# GPIO Setups
led_list = [3,5,7]
GPIO.setup (led_list, GPIO.OUT)
GPIO.output (led_list, 0) #output 0 by default

button_inputs = [11,13]
GPIO.setup (button_inputs, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #pull down inputs

#Set up button functions
def decrease_button(self):
    #Declar global variable locally
    global count
    
    #circles back to max when at 0
    if count == 0:
        count = 7
    else:
        count -= 1
    
def increase_button(self):
    global count
    
    #circles back to min when at 7
    if count == 7:
        count = 0
    else:
        count +=1


#Event detector and debouncing
GPIO.add_event_detect (11, GPIO.RISING, callback = decrease_button, bouncetime = 200)
GPIO.add_event_detect (13, GPIO.RISING, callback = increase_button, bouncetime = 200)



# Logic that you write
def main():
    global count
    
    #converts count to binary string, ensuring that it is 3 characters long
    count_bit = bin(count)[2:].zfill(3)
    
    #sets LED outputs to 0 or 1, depending on the digits
    GPIO.output (3, int(count_bit[0:1]))
    GPIO.output (5, int(count_bit[1:2]))
    GPIO.output (7, int(count_bit[2:3]))
    


# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)

