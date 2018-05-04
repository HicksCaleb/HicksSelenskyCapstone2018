import numpy as np


def mp(arrayX,arrayY,v0=0):
    xGuess = numpy.trapz(arrayX,axis=0)
    yGuess = numpy.trapz(arrayY,axis=1)
    guess = 1/2*xGuess+yGuess
    disagreement = np.abs(xGuess-yGuess)
    return guess,disagreement
