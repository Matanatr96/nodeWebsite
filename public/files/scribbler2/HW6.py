#############################################################################################
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Homework 5//////////////////////////////////////////////#
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Anush Mattapalli///////////////////////////////////////////#
#\\We worked on the homework assignment alone, using only this semester's course materials//#
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\amattapalli3@gatech.edu////////////////////////////////////////#
#\\\\\\\\\\\\\\\\\\\\\\cgbrandys22@gatech.edu - Colin Brandys///////////////////////////////#
#############################################################################################
from Myro import *
import random
import colorsys
from Myro import *
init("COM4")
#setPicSize("small")



def findColor(picture):
    a = []
    G = 0
    R = 0
    W = 0
    B = 0
    Y = 0
    pixmax = 0
    for x in range(0,getWidth(picture)):
        for y in range(0,getHeight(picture)):
            pix = getPixel(picture,x,y)
            r = getRed(pix)
            g = getGreen(pix)
            b = getBlue(pix)
            if r > 120 and g > 120 and b > 120:
                W += 1
            elif r < g and b < g and g > 100:
                G += 1
            elif r > 100 and g > 100 and b < 100 and r > b and g > b:
                Y += 1
            elif g < r and b < r and r > 100:
                R += 1
    pixtot = getWidth(picture) * getHeight(picture)
    G = G / pixtot
    Y = Y / pixtot
    R = R / pixtot
    W = W / pixtot
    print(G,Y,R,W)

    if G > .25:
        pixmax = "Green"
    elif R > .25:
        pixmax = "Red"
    elif Y > .25:
        pixmax = "Yellow"
    elif W > .25:
        pixmax = "White"
    else:
        pixmax = "WHAT COLOR IS THIS?"
    print(pixmax)
    return(pixmax)


def turn():
    x = heads()
    if x == True:
        turnLeft(.683,1)
        setLED("left", "on")
        wait(.5)
        setLED("left", "off")
    else:
        turnRight(.683,1)
        setLED("right", "on")
        wait(.5)
        setLED("right", "off")

def stopLight():
    manualCamera(gain = 50, brightness = 150, exposure = 100)#manual numbers
    p = takePicture()
    show(p)
    color = findColor(p)
    #print("findCOLORsuccessful")
    x = False
    if color == "White":
        stop()
        turn()
    elif color == "Red":
        stop()
        beep(.5,1500)
        return(None)
    elif color == "Yellow":
        forward(.5,2)
    elif color == "Green":
        forward(1,2)
    stopLight()



stopLight()


