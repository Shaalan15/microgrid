from tkinter import *
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(32,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)
GPIO.output(32,GPIO.HIGH)

time.sleep(2)

GPIO.output(40,GPIO.HIGH)
GPIO.output(32,GPIO.LOW)

time.sleep(2)
GPIO.output(40,GPIO.LOW)
GPIO.output(32,GPIO.HIGH)

time.sleep(2)
GPIO.output(40,GPIO.HIGH)
GPIO.output(32,GPIO.LOW)

time.sleep(2)
GPIO.output(40,GPIO.LOW)
GPIO.output(32,GPIO.HIGH)

time.sleep(2)
GPIO.output(40,GPIO.HIGH)
GPIO.output(32,GPIO.LOW)

time.sleep(2)
GPIO.output(40,GPIO.LOW)
GPIO.output(32,GPIO.HIGH)

GPIO.cleanup()
exit()