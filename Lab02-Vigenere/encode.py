import sys
import string


def encode(fileName, keyFile):
    Alphabet = string.ascii_uppercase
    dict = {}
    file1 = open(fileName,'r')
    file2 = open(keyFile,'r')
    newText = ""
    b = ''
    for i in Alphabet:
        dict[i] = ord(i) - 65
    for i in file1.read():
        for k in file2.read():
            print(str(k.upper()))
            print(dict[str(k.upper())])
            print(dict["B"])
    #         newText += chr(ord(i) + dict[k.upper()])
    print(dict)


if __name__ == '__main__':
    encode("temp.txt","temp2.txt")