## What is this?
In this project we'll build a motion detector using a PIR, or a passive infrared sensor. It works by measuring the infrared light radiating from objects in its field of view. It's the same kind of sensor that might be in a motion-activated light.

## How to build it
The motion detector is a pretty simple build. It's almost plug-and-play!

1. Using jumper cables and a breadboard, connect the positive lead of the sensor (the red cable) to the 3.3v output of the Raspberry Pi.
2. Connect the negative lead of the sensor (the black cable) to a ground pin on the Raspberry Pi.
3. Connect the data lead of the sensor (yellow cable) to GPIO pin 4.
4. Run `python motion.py` to start detecting motion.
5. The script should run forever. To stop it, type `ctrl + c`

The PIR sensor can be a little finicky. It detects motion in a wide range, so it may be triggered even if you are beside it or a little behind it. There are two yellow dials on the front of the sensor that affect its sensitivity. Try twisting them different directions and see the results!
