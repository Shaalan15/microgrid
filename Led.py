from tkinter import *
from gpiozero import LED
import RPi.GPIO as GPIO
import tkinter.font
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(32,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)

GPIO.output(32,GPIO.LOW)
GPIO.output(40,GPIO.LOW)

Flag = True

led = LED(14)
led2 = LED(15)
led.on()
led2.on()
