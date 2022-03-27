import string
import sys

def hexFile(fileName):
    hexcode = ""
    finalText = ""
    with open(fileName,'rb') as file:
        hexcode = file.read().hex()
    finalText = ' '.join(hexcode[i:i+2] for i in range(0,len(hexcode),2))
    return finalText

if __name__ == '__main__':
    print(hexFile(sys.argv[1]))
