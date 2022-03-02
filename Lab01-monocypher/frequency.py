import string
import math

def Read(fileName):
    alphabet = list(string.ascii_lowercase)
    dict = {}
    for k in range(26):
        dict[alphabet[k]] = 0
    with open(fileName,'r') as file:
        for i in file.read():
            for k in range(26): 
                if alphabet[k] == i: 
                    dict[alphabet[k]] += 1;  
    return dict

def EuclidianDistance(fileName, baseFile):
    distance = 0
    value = list(Read(fileName).values())
    value2 = list(Read(baseFile).values())
    for i in range(value.count):
        for j in range (value2.count):
            distance += ((value[i] - value2[j]) ** 2)
    return math.sqrt(distance)


values = Read('temp.txt').values()
total = sum(values)
key_list = list(Read('temp.txt').keys())
val_list = list(values)
for i in range(26):
    print(key_list[i] + " " + str(val_list[i]/total))
