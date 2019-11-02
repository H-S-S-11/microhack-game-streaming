# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 11:15:00 2019

@author: pj2g19
"""

import random
import serial
from redinput import readinput

ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM3'
ser.open()

r = random.randint(1,9)
i = 0

while True:
    i = int(readinput())
    if (r>i):
        print("The input was too small")
        
    elif (r<i):
        print("The input was too large")
        
    else:
        print("you guessed correctly")
        break