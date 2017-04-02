#############################################################################################
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Homework 8//////////////////////////////////////////////#
#\\\\\\\\\\\\\\\ Anush Mattapalli & Colin Brandys & Aaron Wasserman/////////////////////////#
#\\We worked on the homework assignment alone, using only this semester's course materials//#
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\amattapalli3@gatech.edu////////////////////////////////////////#
#\\\\\\\\\\\\\\\\\\\\\\cgbrandys22@gatech.edu - Colin Brandys///////////////////////////////#
#\\\\\\\\\\\\\\\\\\\\\a.wasserman@gatech.edu - Aaron Wasserman//////////////////////////////#
#############################################################################################

from Myro import *

setPicSize("small")

def film():
    x = 0
    for sec in timer(20):
        p = takePicture()
        savePicture(p,"Movie{}.png".format(x))
        x = x + 1

    for sec in timer(60):
        p = takePicture()
        savePicture(p,"Movie{}.png".format(x))
        x = x + 1

film()

