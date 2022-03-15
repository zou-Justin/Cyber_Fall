import sys
import string
import math
import os
from Crack import *

def guessKey(fileName):
    file = open(fileName,'r')
    Length = 1
    fileText = file.read()
    file.close()
    strName = "Pile"
    finalText = ""
    actualLength = 0
    actualFinalText = ""
    minimumDistance = 1
    Decode = ""
    for j in range(16):
        piles = [""] * Length
        for i in range(len(fileText)):
                for k in range(Length):
                    if i % Length == k:
                            piles[i%Length] += fileText[i]  
        for i in range(Length):
            Pile1 = piles[i]
            Decode = h(Pile1)
            piles[i] = Decode
        for i in range(len(fileText)):
                finalText += piles[i%Length][i//Length]
        dist = EuclidianDistance(finalText)
        if (dist <= minimumDistance):
            minimumDistance = dist
            actualLength = Length
            actualFinalText = finalText
        finalText = ""
        Length+=1
    return actualLength


if __name__ == '__main__':
    print(guessKey(sys.argv[1]))