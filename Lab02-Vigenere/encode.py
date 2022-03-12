import sys
import string


def encode(fileName, keyFile):
    Alphabet = string.ascii_uppercase
    dict = {}
    file1 = open(fileName,'r')
    file2 = open(keyFile,'r')
    newText = ""
    file1R = file1.read()
    file1Read = ""
    for i in file1R:
        if (i.isupper() or i.islower()):
            file1Read += i
    print(file1Read)
    file2Read = file2.read()
    for i in Alphabet:
        dict[i] = ord(i) - 65
    for i in range(len(file1Read)):
        newText += chr((ord(file1Read[i].upper()) -65 + dict[file2Read[i % len(file2Read)].upper()]) % 26 + 65)
    return newText


if __name__ == '__main__':
    print(encode("temp.txt","temp2.txt"))