#!/usr/bin/python
#!/usr/bin/env python2.7
# script by Alex Eames http://RasPi.tv/
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio
import RPi.GPIO as GPIO
import requests
import logging
# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
logger.debug('This message should go to the log file')

GPIO.setmode(GPIO.BCM)

# GPIO 23 set up as input. It is pulled up to stop false signals
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# print "Make sure you have a button connected so that when pressed"
# print "it will connect GPIO port 23 (pin 16) to GND (pin 6)\n"

print "Waiting for falling edge on port 23"
# now the program will do nothing until the signal on port 23
# starts to fall towards zero. This is why we used the pullup
# to keep the signal high and prevent a false interrupt

print "During this waiting time, your computer is not"
print "wasting resources by polling for a button press.\n"
print "Press your button when ready to initiate a falling edge interrupt."
running = True
off = True
while running:
    try:
        GPIO.wait_for_edge(18, GPIO.FALLING)
        logger.debug('Button pressed, calling IFTTT')
        if off:
            logger.debug('Turning lights on')
            r = requests.get('https://maker.ifttt.com/trigger/meeseeks2/with/key/o69VXHFIIvpjo0CKEbwYNt_OiQbzhyfU-Grlzf8GXdR')
            off = False
        else:
            logger.debug('Turning lights off')
            r = requests.get('https://maker.ifttt.com/trigger/meeseeks/with/key/o69VXHFIIvpjo0CKEbwYNt_OiQbzhyfU-Grlzf8GXdR')
            off = True
    except KeyboardInterrupt:
        GPIO.cleanup()
        running = False
logger.debug('Exiting program')
