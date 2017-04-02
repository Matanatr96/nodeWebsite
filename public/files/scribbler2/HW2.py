# Anush Mattapalli
# amattapalli3@gatech.edu
# Partner: Aaron Wasserman, a.wasserman@gatech.edu
#We worked on the homework assignment alone, using only this semester's course mateials

def quesoForFishy(x):
    y = x // 2.98
    return y

def mailboxes(z):
    min = z * 2
    max = z * 6
    print("Because you have run into",z,"mailbox(es), your car's life has been shortened by anywhere from",min,"to",max,"months.")

def concertTicket():
    cost = float( input("Please input the cost of the ticket"))
    rate = float( input("Please input how much money you make per hour"))
    hours = cost / rate
    print("You need to work {0:.2f} hours to buy your ticket".format(hours))

from math import *
def boringInterlude(x):
    volume = (4/3) * pi * (x**3)
    volumeFeet = volume/1728
    return volumeFeet

def trafficJam(x,y):
    feet = y * 5280
    cars = (feet * x)/15
    return cars

def timeLeft(timeUsed):
    hourLasts = float(input("How long does the battery last?(in hours)"))
    minutes = hourLasts * 60
    percent = ((minutes - timeUsed) / minutes)
    percent= percent *100
    z = int(percent)
    print(z)
    return(minutes - timeUsed)

def daffodils(x,y,z):
    numDozen = (x // 12) +1
    totalCost = numDozen * z
    ourCost = totalCost - y
    print("You will need to contribute ${0:.2f}".format(ourCost))



