#!/usr/bin/python
#!/usr/bin/env python2.7
# script by Alex Eames http://RasPi.tv/
# http://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio
import RPi.GPIO as GPIO
import requests
import logging

# create logger with 'spam_application'
logger = logging.getLogger('interrupt_application')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('interrupt.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level


# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)


logger.info('finished auxiliary_module.Auxiliary.do_something')
logger.info('calling auxiliary_module.some_function()')
logger.info('This message should go to the log file')

GPIO.setmode(GPIO.BCM)

# GPIO 23 set up as input. It is pulled up to stop false signals
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

running = True
off = True
while running:
    try:
        GPIO.wait_for_edge(18, GPIO.FALLING)
        logger.info('Button pressed, calling IFTTT')
        if off:
            logger.info('Turning lights on')
            r = requests.get('https://maker.ifttt.com/trigger/meeseeks2/with/key/o69VXHFIIvpjo0CKEbwYNt_OiQbzhyfU-Grlzf8GXdR')
            off = False
        else:
            logger.info('Turning lights off')
            r = requests.get('https://maker.ifttt.com/trigger/meeseeks/with/key/o69VXHFIIvpjo0CKEbwYNt_OiQbzhyfU-Grlzf8GXdR')
            off = True
    except KeyboardInterrupt:
        GPIO.cleanup()
        running = False
logger.info('Exiting program')
