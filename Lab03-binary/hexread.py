import string
import sys

def hexFile(fileName):
    hexcode = ""
    finalText = ""
    with open(fileName,'rb') as file:
        for i in file.read():
            if len(hex(i).lstrip("0x")) == 1:
                hexcode += "0" + hex(i).lstrip("0x")
            else:
                hexcode += hex(i).lstrip("0x")
    finalText = ' '.join(hexcode[i:i+4] for i in range(0,len(hexcode),4))
    return finalText

if __name__ == '__main__':
    print(hexFile(sys.argv[1]))
