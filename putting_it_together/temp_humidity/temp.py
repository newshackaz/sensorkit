# for pausing the script
from time import sleep
# datetime gets us dates, timedelta for doing math with dates
from datetime import datetime, timedelta
# the main rpi library
import RPi.GPIO as GPIO
# load the sensor library
import Adafruit_DHT as DHT


# set up Rpi numbering system
GPIO.setmode(GPIO.BCM)
# set up sensor
SENSOR = DHT.DHT22
# this is where we read the sensor data
INPUT_PIN = 4


# set up a temp conversion function
def convert_temp(celcius):
    return celcius * float(9) / float(5) + 32

# set up a reading function
def get_reading():
    # get datestring    
    now = datetime.now().strftime("%Y-%m-%d %I:%M %p")
    # get hum and temp from sensor
    humidity, temperature = DHT.read_retry(SENSOR, INPUT_PIN)
    # convert temperature
    temperature = convert_temp(temperature)
    print "temperature = "
    print temperature
    print "humidity = "
    print humidity

# get a reading every 10 seconds
while True:
    get_reading()
    
    sleep(10)

    


