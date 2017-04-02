##########################################################################################
#/////////////////////////////// Anush Mattapalli A02\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
#/////////////////////////////amattapalli3@gatech.edu\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#
#/I worked on the homework assignment alone, using only this semester's course materials\#
##########################################################################################



# "You must be this tall to ride this ride

def tallEnough(x):
    centi = float(x / .39370)
    if (centi > 120)&(centi < 190):
        return True
    else:
        return False

# Finding waldo is easier than you think

def whereIsWaldo(x,y):
    x1 = input("Guess Waldo's x-coordinate")
    y1 = input("Guess Waldo's y-coordinate")
    x1 = int(x1)
    y1 = int(y1)
    if (x1 == x) & (y1 == y):
        print("You found Waldo")
    else:
        print("Couldn't find Waldo. Better luck next time")

# Letter Looping is for little kids

import string


def allLetters(astr):
    seenCount = 0
    index = 0
    while index < len(astr):
        letter = astr[index]
        if letter in string.ascii_letters:
            print(letter)
            index = index + 1
        else:
            index = index + 1

# Letter Replacement should not take this many lines of code

def replaceLetter(aString,aLetter):
    i = 0
    repLet = input("Please input a letter")
    if repLet in aString:
        while i < len(aString):
            if repLet == aString[i]:
                print(aLetter,end="")
                i += 1
            else:
                print(aString[i],end="")
                i += 1
    else:
        while repLet not in aString:
            print("Letter not in string")
            repLet = input("Please input a letter")
        while i < len(aString):
            if repLet == aString[i]:
                print(aLetter,end="")
                i += 1
            else:
                print(aString[i],end="")
                i += 1
    print("")

# Counting is also for little kids

def countUp(x,y,z):
    while x <= y:
        print(x)
        x = x + z



# Mountain ranges are no fun to climb or make

def numMountainRange(x):
    i = 1
    v = 1
    while v <= x:
        i = str(i)
        print(i*v,2*(x-v)*" ",i*v,sep="")
        i = int(i)
        i += 1
        v += 1

# 2 in 1

def printTimestable():

    x = int(input("Input the header"))
    i = 1
    print("Times:",end="")
    a = 1

    while i <= x:
        print(i,"\t",end="")
        i = i + 1
    while a <=x:
        i = 1
        print("")
        print("   ",end="")
        print(a,end="  ")

        while i <= x:
            print(a * i,"\t",end="")
            i = i + 1
        a = a + 1

# same as the last code with a different function call

def printTimes(n):

    n = int(n)
    i = 1
    print("Times:",end="")
    a = 1

    while i <= x:
        print(i,"\t",end="")
        i = i + 1
    while a <=x:
        i = 1
        print("")
        print("   ",end="")
        print(a,end="  ")

        while i <= x:
            print(a * i,"\t",end="")
            i = i + 1
        a = a + 1

printTimestable()








