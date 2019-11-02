# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 13:01:11 2019

@author: pj2g19
"""

import random
import sys
import serial

ser = serial.Serial()
ser.baudrate = 9600
ser.port='COM3'
try:
    ser.open()
except:
    print("failure in connecting to board")
    sys.exit(0)

ser.write(b'5')

print("you ArE goIng to FIgHt A LIon")
print("tHE rEd LIgHtS rEprESEnt your HEALtH")

h = 150
lh = 150
p = 5

while True:
    print("tHE LIon HAS "+ str(lh)+" HEALtH LEFt")
    print("PrESS 1 to FIgHt, 2 to uSE A PotIon")
    print(str(p)+" PotIonS LEFt")
    o = input()
    
    if o == "1":
        c = random.randint(1,10)
        
        if c==1:
            print("your HIt dIdnt ConnECt")
            
        elif c==10:
            print("CrItICAL HIt!")
            lo = lh
            lh = lh - (random.randint(5,15)*2)
            print("you dId "+ str(lo-lh)+" AttAC")
            
            if lh<=0:
                print("you bEAt tHE LIon")
                ser.write(b'0')
                ser.close()
                sys.exit(0)
            
        else:
            lo = lh
            lh = lh - random.randint(5,15)
            print("you dId "+str(lo-lh)+" AttAC")
            
            if lh<=0:
                print("you bEAt tHE LIon")
                ser.write(b'0')
                ser.close()
                sys.exit(0)
            
    
    elif o == "2" and p>0:
        p = p-1
        ho = h
        h = h+50
        
        if h>150:
            h=150
        
        print("you rEStorEd "+str(h-ho)+" HEALtH")
        
    
    else:
        print("Error - not An InPut")
        
    c = random.randint(1,10)
    if c==1:
        print("tHE LIon dIdnt AttAC")
        
    elif c==10:
        print("tHE LIon dId A CrItICAL HIt")
        ho = h
        h = h-(random.randint(15,30)*2)
        print("tHE LIon dId "+str(ho-h)+" AttAC")
        
        if h<=0:
            ser.write(b'0')
            print("you dIE")
            ser.close()
            sys.exit(0)
        
    else:
        ho = h
        h = h-random.randint(15,30)
        print("tHE LIon dId "+str(ho-h)+" AttAC")
        
        if h<=0:
            ser.write(b'0')
            print("you dIE")
            ser.close()
            sys.exit(0)
            
    if(h>=120):
        ser.write(b'5')
    elif(h>=90):
        ser.write(b'4')
    elif(h>=60):
        ser.write(b'3')
    elif(h>=30):
        ser.write(b'2')
    elif(h>0):
        ser.write(b'1')