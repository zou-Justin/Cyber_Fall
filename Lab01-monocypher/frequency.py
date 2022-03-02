import string
import math

def Read(fileName):
    alphabet = list(string.ascii_letters)
    dict = {}
    for k in range(52):
        dict[alphabet[k]] = 0
    with open(fileName,'r') as file:
        for i in file.read():
            for k in range(52): 
                if alphabet[k] == i: 
                    dict[alphabet[k]] += 1;  
    return dict

def EuclidianDistance(fileName, baseFile):
    distance = 0
    value = list(Read(fileName).values())
    value2 = list(Read(baseFile).values())
    for i in range(len(value)):
        distance += ((value[i] - value2[i]) ** 2)
    return math.sqrt(distance)

print(EuclidianDistance("temp.txt","temp2.txt"))

# values = Read('temp.txt').values()
# total = sum(values)
# key_list = list(Read('temp.txt').keys())
# val_list = list(values)
# for i in range(52):
#     print(key_list[i] + " " + str(val_list[i]/total))
