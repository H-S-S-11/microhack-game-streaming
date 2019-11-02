# -*- coding: utf-8 -*-
"""
created on Sat Nov  2 13:01:11 2019

@author: pj2g19
"""

import random
import sys
import serial
from padinput import readinput

ser = serial.Serial()
ser.baudrate = 9600
ser.port='COM3'
ser.open()
ser.write(b'5')
ser.close()

print("you are going to fight a lion")
print("the red lights represent your health")

h = 100
lh = 150
p = 5

while True:
    print("the lion has "+ str(lh)+" health left")
    print("press 1 to fight, 2 to use a potion")
    print(str(p)+" potions left")
    print()
    o = readinput()
    
    if o == "1":
        c = random.randint(1,10)
        
        if c==1:
            print("your attack missed")
            
        elif c==10:
            print("critical hit!")
            lo = lh
            lh = lh - (random.randint(5,15)*2)
            print("you did "+ str(lo-lh)+" damage")
            print()
            
            if lh<=0:
                print("you beat the lion")
                ser.open()
                ser.write(b'0')
                ser.close()
                sys.exit(0)
            
        else:
            lo = lh
            lh = lh - random.randint(5,15)
            print("you did "+str(lo-lh)+" damage")
            print()
            
            if lh<=0:
                print("you beat the lion")
                ser.open()
                ser.write(b'0')
                ser.close()
                sys.exit(0)
            
    
    elif o == "2" and p>0:
        p = p-1
        ho = h
        h = h+50
        
        if h>150:
            h=150
        
        print("you restored "+str(h-ho)+" health")
        print()
        
    
    else:
        print("error - not an input")
        
    c = random.randint(1,10)
    if c==1:
        print("the lion missed")
        
    elif c==10:
        print("the lion did a critical hit")
        ho = h
        h = h-(random.randint(15,30)*2)
        print("the lion did "+str(ho-h)+" damage")
        print()
        
        if h<=0:
            ser.open()
            ser.write(b'0')
            print("you died")
            ser.close()
            sys.exit(0)
        
    else:
        ho = h
        h = h-random.randint(15,30)
        print("the lion did "+str(ho-h)+" damage")
        print()
        
        if h<=0:
            ser.open()
            ser.write(b'0')
            print("you died")
            ser.close()
            sys.exit(0)
            
    if(h>=120):
        ser.open()
        ser.write(b'5')
        ser.close()
    elif(h>=90):
        ser.open()
        ser.write(b'4')
        ser.close()
    elif(h>=60):
        ser.open()
        ser.write(b'3')
        ser.close()
    elif(h>=30):
        ser.open()
        ser.write(b'2')
        ser.close()
    elif(h>0):
        ser.open()
        ser.write(b'1')
        ser.close()