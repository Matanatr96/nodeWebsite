#########################################################################################
#Avoid Walls
#Anush Mattapalli & Aaron Wasserman
#amattapalli3@gatech.edu, a.wasserman@gatech.edu
#We worked on the homework assignment alone, using only this semester's course materials
#########################################################################################

from Myro import *

def avoidWalls():
    for seconds in timer(65):
        while (getObstacle("center") < 500):
            translate(1)
        beeper = getObstacle("center")
        beep(.25, beeper *5)
        backward(.35,.5)
        turnRight(.35,1)
    celebration()


def celebration():
    rotate(1)
    beep(1,1600)
    forward(1,.5)
    beep(.5,800)
    backward(1,.5)
    beep(.125,1000)
    turnLeft(.35,1)
    beep(.25,1200)
    turnRight(.35,1)
    beep(.75,1400)
    rotate(0)

avoidWalls()