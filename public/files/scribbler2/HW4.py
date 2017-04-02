##########################################################################################
# Anush Mattapalli
# amattapalli3@gatech.edu
# HW4.py
# I worked on the homework assignment alone, using only this semester's course materials.
##########################################################################################
from Myro import *
init("COM4")

# I can do tricks too
def morningRoutine(x):
    tune()

    if x == 1:
        trick1()
    elif x == 2:
        trick1()
        beep(2,2000)
        trick2()
    elif x == 3:
        trick1()
        beep(2,2000)
        trick2()
        beep(2,2000)
        trick3()
    elif x == 4:
        trick1()
        beep(2,2000)
        trick2()
        beep(2,2000)
        trick3()
        beep(2,2000)
        trick4()
    elif x > 4:
        trick1()
        beep(2,2000)
        trick2()
        beep(2,2000)
        trick3()
        beep(2,2000)
        trick4()
        beep(2,2000)
        tune()

# This is also what i do in the morning
def greetMenu():
    print("1. Tiny Treats")
    print("2. OK Treats")
    print("3. Jumbo Treats")
    print("")
    print("0. Exit")

    x = 9
    while (x > 3) or (x < 0):
        x = int(input("Which option would you like?"))
        if (x > 3) or (x < 0):
            print("I'm sorry, I cannot accept that.")

    if x == 3:
        morningRoutine(5)
    elif x == 2:
        morningRoutine(3)
    elif x == 1:
        morningRoutine(1)
    else:
        print("Bye, bye! Have a good day!")

# go get the stick scribby
def trick1():
    forward(1,3)
    motors(-1,1)
    wait(1.3)
    forward(1,3)
    rotate(1)
    wait(2)
    beep(1,600)
    beep(1,700)
    beep(1,500)
    beep(1,400)
    stop()

# NOOOOOOOOOOO SCRIBBBBY DONT DIEEEEEE
def trick2():
    for seconds in timer(10):
        forward(1,1)
        motors(.7,1,2)
        backward(1,1)
        motors(1,.7,1.8)
    stop()
    x = 2000
    rotate(1)
    while x > 0:
        beep(.05,x)
        x = x - 100
    stop()

# Stop it scribby, thats not beef jerky
def trick3():
    forward(2,1)
    wait(1)
    motors(.05,1,10)
    stop()

# Dont Break ANYTHING
def trick4():
    for seconds in timer(20):
        while (getObstacle("center") < 500):
            translate(1)
        beeper = getObstacle("center")
        beep(.25, beeper *10)
        backward(.35,.5)
        turnRight(.35,1)

# Mario TIME!!!
def tune():
    beep(.1,1300)
    beep(.2,1300)
    beep(.2,1300)
    beep(.1,1046)
    beep(.2,1300)
    beep(.4,1560)
    beep(.2,2*523)

    #unhashtag if longer tune is needed
    #beep(.2,2*329)
    #beep(.2,2*261)
    #beep(.1,2*349)
    #beep(.1,2*493)
    #beep(.05,2*466)
    #beep(.05,2*349)

    #beep(.2,2*329)
    #beep(.1,1300)
    #beep(.2,1560)
    #beep(.2,1760)
    #beep(.2,1400)
    #beep(.2,1560)
    #beep(.1,1300)
    #beep(.2,2*523)
    #beep(.2,2*587)
    #beep(.1,2*493)

greetMenu()