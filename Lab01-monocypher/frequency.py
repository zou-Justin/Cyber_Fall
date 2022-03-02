import string
import math
import sys

def Read(fileName = sys.argv[0]):
    alphabet = list(string.ascii_lowercase)
    dict = {}
    for k in range(26):
        dict[alphabet[k]] = 0
    with open(fileName,'r') as file:
        for i in file.read():
            for k in range(26): 
                if alphabet[k] == i.lower(): 
                    dict[alphabet[k]] += 1;  
    return dict

def EuclidianDistance(fileName = sys.argv[0], baseFile = sys.argv[1]):
    distance = 0
    value = list(Read(fileName).values())
    value2 = list(Read(baseFile).values())
    for i in range(len(value)):
        distance += ((value[i] - value2[i]) ** 2)
    return math.sqrt(distance)

print(EuclidianDistance("temp.txt","temp2.txt"))

def printStuff():
    values = Read('temp.txt').values()
    total = sum(values)
    key_list = list(Read('temp.txt').keys())
    val_list = list(values)
    for i in range(26):
        print(key_list[i] + " " + str(val_list[i]/total))
printStuff()