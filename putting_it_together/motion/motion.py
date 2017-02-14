from time import sleep
import RPi.GPIO as GPIO

# set up board numbering system
GPIO.setmode(GPIO.BCM)
# this is the pin we read data from (bottom right)
INPUT_PIN = 21
# set up sensor 

# set up the data pin to accept data
GPIO.setup(INPUT_PIN, GPIO.IN, GPIO.PUD_DOWN)

while True:
    # take reading
    current_reading = GPIO.input(INPUT_PIN)
    
    # current_reading will be a 1 or 0. 1 means motion
    if (current_reading == 1):
        print "MOTION DETECTED"
    else:
        print "..."
    
    # wait two seconds:
    sleep(1)
