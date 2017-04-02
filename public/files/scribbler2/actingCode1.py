#############################################################################################
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Homework 8//////////////////////////////////////////////#
#\\\\\\\\\\\\\\\ Anush Mattapalli & Colin Brandys & Aaron Wasserman/////////////////////////#
#\\We worked on the homework assignment alone, using only this semester's course materials//#
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\amattapalli3@gatech.edu////////////////////////////////////////#
#\\\\\\\\\\\\\\\\\\\\\\cgbrandys22@gatech.edu - Colin Brandys///////////////////////////////#
#\\\\\\\\\\\\\\\\\\\\\a.wasserman@gatech.edu - Aaron Wasserman//////////////////////////////#
#############################################################################################

## from Myro import *
## ##
## init("COM5")
## 
def attacker():

    from Myro import *
    forward(.2,10)

    motors(.2,.1, 7)

    motors(.1,.2,7)

    forward(.2,6)

    forward(.2,4)

    backward(.2,5)

    turnRight(.2,12)

    motors(.5,.1, 7)

    motors(.1,.5, 7)

    forward(.2,1)

    backward(.2,1)

    turnLeft(.2,10)

    turnRight(.2,10)

    forward(.2,10)

    turnRight(.2,100)
