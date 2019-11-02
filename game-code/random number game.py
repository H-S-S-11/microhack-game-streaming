# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 11:15:00 2019

@author: pj2g19
"""

import random

r = random.randint(1,10)
i = 0

while not (i == r):
    i = int(input())
    if (r>i):
        print("The input was too small")
        
    elif (r<i):
        print("The input was too large")
        
    else:
        print("you guessed correctly")