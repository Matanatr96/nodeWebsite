#############################################################################################
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Homework 5//////////////////////////////////////////////#
#\\\\\\\\\\\\\\\ Anush Mattapalli & Colin Brandys & Aaron Wasserman/////////////////////////#
#\\We worked on the homework assignment alone, using only this semester's course materials//#
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\amattapalli3@gatech.edu////////////////////////////////////////#
#\\\\\\\\\\\\\\\\\\\\\\cgbrandys22@gatech.edu - Colin Brandys///////////////////////////////#
#\\\\\\\\\\\\\\\\\\\\\a.wasserman@gatech.edu - Aaron Wasserman//////////////////////////////#
#############################################################################################

from Myro import *

#play("Toothless Lost.wav")

def picPuller():

    movie = []
    for y in range(0, pics):
        movie.append(y)
    print(len(movie))
    print("finished appending")
    for x in range(0, pics):
        movie[x] = makePicture("Movie{}.png".format(x))
        print("appended", x)
        show(movie[x])

    savePicture(movie,"Movie1.gif")

picPuller(72)
# number of pics plus 1