#############################################################################################
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Homework 8//////////////////////////////////////////////#
#\\\\\\\\\\\\\\\ Anush Mattapalli & Colin Brandys & Aaron Wasserman/////////////////////////#
#\\We worked on the homework assignment alone, using only this semester's course materials//#
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\amattapalli3@gatech.edu////////////////////////////////////////#
#\\\\\\\\\\\\\\\\\\\\\\cgbrandys22@gatech.edu - Colin Brandys///////////////////////////////#
#\\\\\\\\\\\\\\\\\\\\\a.wasserman@gatech.edu - Aaron Wasserman//////////////////////////////#
#############################################################################################

from Myro import *

def defenderRobot1():
    backward(.05, 24)
    stop()
    turnLeft(.2,2.5)
    turnRight(.2,2.5)
    wait(4)
    forward(.1,12)

defenderRobot1()

