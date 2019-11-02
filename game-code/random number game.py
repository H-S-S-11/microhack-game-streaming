# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 11:15:00 2019

@author: pj2g19
"""

import random, time, serial, sys
from padinput import readinput

ser = serial.Serial()
ser.port = 'COM3'
ser.baudrate = 9600
ser.open()
ser.write(b'5')
ser.close()

r = random.randint(1,9)
i = 0
l = 5

while l>0:
    i = int(readinput())
    if (r>i):
        print("The input was too small")
        l = l-1
        ser.open()
        ser.write(bytes(str(l), "ascii"))
        ser.close()
        
    elif (r<i):
        print("The input was too large")
        l = l-1
        ser.open()
        ser.write(bytes(str(l), "ascii"))
        ser.close()
        
    else:
        print("you guessed correctly")
        sys.exit(0)
    
    time.sleep(1)
    
ser.open()

g=30
while(g>0):
    ser.write(b'5')
    time.sleep(0.2)
    ser.write(b'0')
    g=g-1
    
ser.close()