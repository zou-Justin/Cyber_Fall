import string
import sys

def hexFile(fileName):
    hexcode = ""
    finalText = ""
    alphabet = list(string.ascii_lowercase)
    with open(fileName,'r') as file:
        for i in file.read():
            if len(hex(ord(i)).lstrip("0x")) == 1 and hex(ord(i)).lstrip("0x").isalpha():
                hexcode += "0" + hex(ord(i)).lstrip("0x")
            else:
                hexcode += hex(ord(i)).lstrip("0x")
    finalText = ' '.join(hexcode[i:i+4] for i in range(0,len(hexcode),3))
    return finalText


print(hexFile('test.txt'))
print(hex(1))
