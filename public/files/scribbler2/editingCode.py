#############################################################################################
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Homework 8//////////////////////////////////////////////#
#\\\\\\\\\\\\\\\ Anush Mattapalli & Colin Brandys & Aaron Wasserman/////////////////////////#
#\\We worked on the homework assignment alone, using only this semester's course materials//#
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\amattapalli3@gatech.edu////////////////////////////////////////#
#\\\\\\\\\\\\\\\\\\\\\\cgbrandys22@gatech.edu - Colin Brandys///////////////////////////////#
#\\\\\\\\\\\\\\\\\\\\\a.wasserman@gatech.edu - Aaron Wasserman//////////////////////////////#
#############################################################################################

from Myro import *

def fade(x,y):
    pics = y - x
    num = x - 1
    for i in range(0,pics):
        num = num + 1
        print(num)
        p = makePicture("Movie{}.png".format(num))
        for x in range(0,getWidth(p)):
            for y in range(0,getHeight(p)):
                pix = getPixel(p,x,y)
                r = getRed(pix)
                g = getGreen(pix)
                b = getBlue(pix)
                per = 255 / pics
                setRed(pix,r - per * (i+1))
                setGreen(pix,g - per * (i+1))
                setBlue(pix,b - per * (i+1))
        show(p)
        savePicture(p,"Movie{}.png".format(num))



#starting frame, ending frame + 1

def seeingRed(a,b):
    pictures = b - a
    number = a - 1
    for s in range(0,pictures):
        number = number + 1
        print(number)
        l = makePicture("Movie{}.png".format(number))
        for a in range(0,getWidth(l)):
            for b in range(0,getHeight(l)):
                pixel = getPixel(l,a,b)
                setRed(pixel, 255)
        show(l)
        savePicture(l,"Movie{}.png".format(number))


#starting frame, ending frame + 1

def negativeColors(c,d):
    from Myro import *
    picture = d - c
    nums = c - 1
    for h in range(0,picture):
        nums = nums + 1
        print(nums)
        s = makePicture("Movie{}.png".format(nums))
        for c in range(0,getWidth(s)):
            for d in range(0,getHeight(s)):
                picks = getPixel(s,c,d)
                r = getRed(picks)
                g = getGreen(picks)
                b = getBlue(picks)
                R=255-int(r)
                B=255-int(b)
                G=255-int(g)
                setRed(picks,R)
                setBlue(picks,B)
                setGreen(picks,G)
        show(s)
        savePicture(s,"Movie{}.png".format(nums))



#starting frame, ending frame + 1

# uncomment to run
#fade(65,72)
#seeingRed(49,55)
#negativeColors(34,42)





