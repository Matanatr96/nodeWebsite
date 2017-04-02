# 8/28/14
# HW1.py
# Anush Mattapalli A02
# amattapalli3@gatech.edu
# I worked on the homework assignment alone, using only this semester's course materials

import math

def machToFPS():
    x=int(input("Please enter the speed in mach"))
    y=x * 1116.4370079
    print (x, "mach is equal to", y, "feet per second.")


def sqPyramidVolume():
    length=input("Please input the length of the base in inches")
    height=input("Please input the height of the pyramid in inches")
    length=float(length)
    height=float(height)
    volume = ((length ** 2)*(height))//3
    print ("The volume of the square pyramid is", volume , "inches cubed.")


def makeChange():
    cents=int(input("Please input the number of cents"))
    dollars=cents//100
    leftOne=cents-(dollars*100)
    quarters=leftOne//25
    leftTwo=leftOne-(quarters*25)
    dimes=leftTwo//10
    leftThree=leftTwo-(dimes*10)
    nickels=leftThree//5
    leftFour=leftThree-(nickels*5)
    pennies=leftFour
    print("You have", dollars, "dollars ", quarters, "quarters", dimes,"dimes", nickels, "nickels", pennies, "pennies")

def PPIIndex():
    weight=float(input("Please enter your weight in pounds"))
    height=float(input("Please enter your height in inches"))
    ppi=(weight/(height*1.125))
    b="{:.1f}".format(ppi)
    print("Your corrected PPI is",b,".", sep="")


