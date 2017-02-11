# for pausing the script
from time import sleep
# datetime gets us dates, timedelta for doing math with dates
from datetime import datetime, timedelta
# the main rpi library
import RPi.GPIO as GPIO
# load the sensor library
import Adafruit_DHT as DHT
# load the csv writing module
import csv

# set up Rpi numbering system
GPIO.setmode(GPIO.BCM)
# set up sensor
SENSOR = DHT.DHT22
# this is where we read the sensor data
INPUT_PIN = 4

# store the csv name because we'll use it later
DATACSV = 'test_data.csv'

# set up a temp conversion function
def convert_temp(celcius):
    return celcius * float(9) / float(5) + 32

# check csv for a header:
def check_header():
    # open csv for reading
    try:
        mycsv = open(DATACSV, 'rb')
    except:
        # open csv for writing:
	mycsv = open(DATACSV, 'wb')
	# make the csv writer object
	writer = csv.writer(mycsv)
	# write the header row
	writer.writerow(['date', 'temperature', 'humidity'])

# set up a reading function
def get_reading():
    # get datestring    
    now = datetime.now().strftime("%Y-%m-%d %I:%M %p")
    # get hum and temp from sensor
    humidity, temperature = DHT.read_retry(SENSOR, INPUT_PIN)
    # convert temperature
    temperature = convert_temp(temperature)
    print "temperature = {0}".format(temperature)
    print "humidity = {0}".format(humidity)
    
    myCsv = open(DATACSV, 'a')
    csvWriter = csv.writer(myCsv)
    csvWriter.writerow([now, round(temperature, 2), round(humidity, 2)])
    myCsv.close()

check_header()
# get a reading every 10 seconds
while True:
    get_reading()
    sleep(60)
