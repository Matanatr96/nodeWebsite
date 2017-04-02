#############################################################################################
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Homework 5//////////////////////////////////////////////#
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Anush Mattapalli///////////////////////////////////////////#
#\\\I worked on the homework assignment alone, using only this semester's course materials//#
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\amattapalli3@gatech.edu////////////////////////////////////////#
#############################################################################################

from Graphics import *
from Myro import *

init("COM4")

# I'm Free of these restraining programs :D
# IMPORTANT---- Move the robot for only 5 seconds
# Then close the window opened by calico

f = open("myMovements.txt","w")

def handleKeyPress(win, event):
    x = getKeyPressed()
    if (x == "Up"):
        forward(1,.1)
        f.write("forward .1 ")
        f.write(str(get("light",0)))
        f.write("\n")
    elif (x == "Down"):
        backward(1,.1)
        f.write("backward .1 ")
        f.write(str(get("light",0)))
        f.write("\n")
    elif (x == "Right"):
        turnRight(1,.1)
        f.write("turnRight .1 ")
        f.write(str(get("light",0)))
        f.write("\n")
    elif (x == "Left"):
        turnLeft(1,.1)
        f.write("turnLeft .1 ")
        f.write(str(get("light",0)))
        f.write("\n")
    elif (x == "space"):
        stop()
    elif (x == "b"):
        beep(.5,1500)
        f.write("beep .1")
        f.write("\n")
    else:
        print("Try The Arrow Keys")

def handleKeyRelease(win, event):
    x = getKeyPressed()
    if (x == "Right"):
        stop()
        print("stopped")
    elif (x == "Left"):
        stop()
        print("stopped")





# "Ill Take It From Here" - Scribby

def startTheAutomation():
    win = Window()
    onKeyPress(handleKeyPress)
    onKeyRelease(handleKeyRelease)
    wait(10)
    f.close()
    print("closed")

def collectData(theFile,direc):
    f = open(theFile,"r")
    line = f.readline()
    d = 0
    t = 0
    b = 0
    while(len(line) > 0):
        x = line.split(" ")
        time = x[1]
        direction = x[0]
        if direction == direc:
            d = d + 1
        elif direction == "beep":
            b = b + 1
        t += .1
        line = f.readline()

    f.close()
    print("The robot travelled for", t ,"seconds total, beeping", b,"times. This robot moved", direc,",", d,"times.")


startTheAutomation()
collectData("myMovements.txt","backward")

def replay(filename):
    f = open(filename,"r")
    line = f.readline()
    while(len(line) > 0):
        x = line.split(" ")
        time = x[1]
        direction = x[0]
        if direction == "forward":
            forward(1,.1)
        elif direction == "backward":
            backward(1,.1)
        elif direction == "turnRight":
            turnRight(1,.1)
        elif direction == "turnLeft":
            turnLeft(1,.1)
        else:
            beep(.5,1500)
        line = f.readline()
    f.close()

replay("myMovements.txt")

