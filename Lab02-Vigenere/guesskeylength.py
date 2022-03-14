import sys
import string
import math
import os
from Crack import *


# def Decypher(fileName):
#     file = open(fileName,'r')
#     Length = 1
#     fileText = file.read()
#     file.close()
#     strName = "Pile"
#     finalText = ""
#     actualFinalText = ""
#     minimumDistance = 1
#     Decode = ""
#     for j in range(5):
#         piles = [""] * Length
#         for i in range(len(fileText)):
#             for k in range(Length):
#                 if i % Length == k:
#                     piles[i%Length] += fileText[i]
#         for i in range(Length):
#             Pile1 = open(strName + str(i),'w')
#             Pile1.write(piles[i%Length])
#             Pile1.close()
#             Decode = decode(strName + str(i))
#             for i in range(len(Decode)):
#                 finalText += piles[i % Length][i//Length]
#         pile23 = open('newText.txt','w')
#         pile23.write(finalText)
#         pile23.close()
#         dist = EuclidianDistance('newText.txt',"temp.txt")
#         if (dist <= minimumDistance):
#             minimumDistance = dist
#             p = open('newText.txt','r')
#             actualFinalText = p.read()
#             p.close()
#         finalText = ""
#         for i in range(Length):
#             os.remove(strName + str(i))
#         Length+=1
#         os.remove('newText.txt')
#     return Length