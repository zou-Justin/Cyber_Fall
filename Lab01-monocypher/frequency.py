import string
import sys

def Read(fileName):
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

def printStuff(file):
    values = Read(file).values()
    total = sum(values)
    key_list = list(Read(file).keys())
    val_list = list(values)
    for i in range(26):
        print(key_list[i] + " " + str(val_list[i]/total))


if __name__ == '__main__':
    printStuff(sys.argv[1])