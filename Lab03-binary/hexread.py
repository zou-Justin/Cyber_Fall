import string
import sys

def hexFile(fileName):
    hexcode = ""
    finalText = ""
    with open(fileName,'rb') as file:
        hexcode = file.read().hex()
    finalText = ' '.join(hexcode[i:i+4] for i in range(0,len(hexcode),4))
    return finalText

if __name__ == '__main__':
    print(hexFile(sys.argv[1]))
