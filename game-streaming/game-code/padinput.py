# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 19:26:55 2019

@author: aimeeelisabeth
"""

def readinput():
    import serial
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = 'COM3'
    ser.open()
    inp = str(ser.read(3))
    
    col = inp[-3]
    row = inp[-2]
    
    if col=="0":
        if row=="0":
            return "1"
        elif row=="1":
            return "4"
        elif row=="2":
            return "7"
        elif row=="3":
            return "A"
    elif col=="1":
        if row=="0":
            return "2"
        elif row=="1":
            return "5"
        elif row=="2":
            return "8"
        elif row=="3":
            return "0"
    elif col=="2":
        if row=="0":
            return "3"
        elif row=="1":
            return "6"
        elif row=="2":
            return "9"
        elif row=="3":
            return "B"
    elif col=="3":
        if row=="0":
            return "F"
        elif row=="1":
            return "E"
        elif row=="2":
            return "D"
        elif row=="3":
            return "C"
        
    ser.reset_input_buffer()
    ser.close()

    