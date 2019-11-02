# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
import serial

ser = serial.Serial()
ser.baudrate = 9600
ser.port('COMP3')
try:
    ser.open
except:
    print("failure in connecting to board")
    sys.exit(0)

print("you are going to FIght bad guyS")

i1 = "dagger" #i1 and i2 stand for item 1 and item 2
i2 = "fireball"
print("")

print("you can uSe a dagger or a FIreball to FIght")
print("IF your health hitS 0 you loSe")
print("you Start at 150 health")
print("you can uSe potIonS to reStore 75 health")
print("the FIreball uSeS Strength but IS a Stronger attacc")
print("you reStore 10 strength each turn")
print("you can uSe Strength potionS to reStore 50 Strength")
print("the Stronger the bad guy you Fight the larger currency you get")
print("")


du=False #these variables are used in order to check who has been fought and who is left to fight
ca=False
fo=False
sn=False
hw=False
ele=False
rh=False
ho=False
sh=False
rsh=False

my = random.randint(10,20) #my is the amount of money the player has, to start, they have between 10 and 20

h = 150 #h is player health
s = 100
hp = 5 #number of potions remaining
sp = 5 #number of strength potions remaining
r = 5 #r is the max number of rounds
rn = 1 #rn is the current round number
x = 0

i1d = random.randint(5,15) #this is the damage item 1 and item 2 will do
i2d = random.randint(15,30)

while not(h<=0) or not (r==0):

    while not x == rn and x != 5:

        mid = random.randint(1,10)

        if (mid == 1) and not du == True:
            m = "duck"
            mh = 30
            dm = 1
            dx = 10
            x=x+1
            du = True
            pm = 1
            px = 10

        elif (mid == 2) and not ca == True:
            m = "cat"
            mh = 40
            dm = 5
            dx = 10
            x=x+1
            ca = True
            pm = 3
            px = 13

        elif (mid == 3) and not fo == True:
            m = "fox"
            mh = 50
            dm = 7
            dx = 15
            x=x+1
            fo = True
            pm = 6
            px = 16

        elif (mid == 4) and not sn == True:
            m = "snake"
            mh = 60
            dm = 9
            dx = 15
            x=x+1
            sn = True
            pm = 7
            px = 17

        elif (mid == 5) and not hw == True:
            m = "hawk"
            mh = 70
            dm = 10
            dx = 15
            x=x+1
            hw = True
            pm = 9
            px = 19

        elif (mid == 6) and not ele == True:
            m = "elephant"
            mh = 80
            dm = 15
            dx = 17
            x=x+1
            ele = True
            pm = 11
            px = 21

        elif (mid == 7) and not rh == True:
            m = "rhino"
            mh = 90
            dm = 15
            dx = 17
            x=x+1
            rh = True
            pm = 12
            px = 22

        elif (mid == 8) and not ho == True:
            m = "hippo"
            mh = 100
            dm = 17
            dx = 20
            x=x+1
            ho = True
            pm = 15
            px = 25

        elif (mid == 9) and not sh == True:
            m = "shark"
            mh = 110
            dm = 15
            dx = 22
            x=x+1
            sh = True
            pm = 17
            px = 27

        elif (mid == 10) and not rsh == True:
            m = "really big shark"
            mh = 120
            dm = 20
            dx = 25
            x=x+1
            rsh = True
            pm = 20
            px = 30
            
        if x==5:
            break
    
    print("round "+str(rn))
    print("you will fight a "+m+" with "+str(mh)+" health")
    print("to Fight the "+m+" type '1', to uSe a fireball, type '2', to use a health potion, press '3' and to use a strength potion, press 'F'")

    while not (mh <= 0) or not (h <= 0):
        print("")
        print("")
        print("your health "+str(h))
        print("your Strength "+str(s))
        print(m+" health: "+str(mh))
        print("you have "+str(hp)+" health potions remaining")
        print("you have "+str(sp)+" strength potions remaining")
    
        i = input()
        print("")
    
        if i == "1":
        
            c = random.randint(1,10)
        
            if c == 1:
               print("you miss")
        
            elif c == 10:
                print ("critical hit")
                mho = mh
                mh = (mh-(2*i1d))
                print("you did "+str(mho-mh)+" damage")
            
            else:
                mho = mh
                mh = (mh-i1d)
                print("you did "+str(mho-mh)+" damage")
            
        if i=="2":
            
            
        
        if i == "3" and hp>0 and h<150:
            oh = h
            h = h+75
            hp = hp-1
            
            if h>150:
                h = 150
            print("you used a potion and restored "+str(h-oh)+" health")
        
        h = (h-random.randint(dm,dx))
    
        if mh <= 0:
            print("you won the fight")
            mo = my
            my = my+random.randint(pm,px)
            print("you won "+str(my-mo)+" money")
            print("")
            break
        
        elif h <= 0:
            print("you lost")
            break
    
    if h<=0 or x==5:
        break
    
    if h>0 and r>0:
        r = r-1
        rn = rn+1

        ch = ""
        print("welcome to the shop, you can buy potions and weapon upgrades here")
        while not ch == "leave":
            print("1 potion costs 10 money and one weapon costs 15 money")
            print("to buy a potion, type 'potion', to buy an upgrade, type 'upgrade' and to leave, type 'leave'")
            print("you have "+str(my)+" money")
            print("What yould you like to buy?")
            ch = input("")
            print("")

            if ch == "potion" and my >=10:
                hp = hp+1
                my = my-10
                print("you bought 1 potion")
                print("")

            elif ch == "potion" and my <10:
                print("you dont have enough money to buy a potion")
                print("")

            if ch == "upgrade" and my>=15:
                i1d = i1d+5
                i2d = i2d+5
                my = my-15
                print("your weapon damage increased by 5")
                print("")

            elif ch == "upgrade" and my<15:
                print("you dont have enough money to buy an upgrade")
                print("")

            if ch == "leave":
                print("you left the shop")
                print("")
                break
        
        
        print("")
        print("you have "+str(h)+" health remaining and "+str(hp)+" potions remaining, how many would you like to use?")
        up = "a"
        while not up.isdigit():
            up = input("")
            print("")
        
        up = int(up)
        oh = h
        if (up<hp):
            h = (h+(75*up))
            hp=hp-up
        else:
            h = h+(75*hp)
            hp=0
    
        if h>150:
            h = 150
    
        print("you restored "+str(h-oh)+" health")
        print("your Strength is also completely reStored")
        s = 100
        print("")
        print("")
    
if x==5:
    print("")
    print("congratulations, you won!")
    print("thank you for playing")
input()
