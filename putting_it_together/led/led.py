# this library lets you control the pins
import Rpi.GPIO as GPIO
# this library will let us pause the program
from time import sleep

# set the Pi to use BCM numbering, not "physical" numbering
GPIO.setmode(GPIO.BCM)

# this pin will power the led
POWER_PIN = 17

# set up the pin to output power
GPIO.setup(POWER_PIN, GPIO.OUT)

# this creates an infinite loop
while True:
    # send power through the pin
    GPIO.output(POWER_PIN, True)
    # chill
    sleep(1)
    # cut power off
    GPIO.output(POWER_PIN, False)
    # chill
    sleep(1)



