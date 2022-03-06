from frequency import Read
from distance import EuclidianDistance
import sys

#reverse alphabet is a different case from simply shifiting down by 1 so account for it
def decode(Caesar_text = sys.argv[1]):
    newText = ""
    file = ""
    minimumDistance = 1000
    shiftedText = ""
    for i in range(26):
        dist = EuclidianDistance(Caesar_text,"temp.txt")
        file = open(Caesar_text,'r')
        fileRead = file.read()
        file.close()
        if (dist < minimumDistance):
            minimumDistance = dist
            newText = fileRead
        shiftedText = shift(fileRead)
        wFile = open(Caesar_text, "w")
        wFile.write(shiftedText)
        wFile.close()
    file2 = open(Caesar_text,'r')
    fileRead = file2.read()
    file2.close()
    shiftedText = reverseShift(fileRead)
    wFile = open(Caesar_text, "w")
    wFile.write(shiftedText)
    wFile.close()
    for i in range(26):
        dist = EuclidianDistance(Caesar_text,"temp.txt")
        file = open(Caesar_text,'r')
        fileRead = file.read()
        file.close()
        if (dist < minimumDistance):
            minimumDistance = dist
            newText = fileRead
        shiftedText = shift(fileRead)
        wFile = open(Caesar_text, "w")
        wFile.write(shiftedText)
        wFile.close()
    return newText

def reverseShift(Text):
    text = ""
    for char in Text:
        if (char.isupper()):
            text += chr(25 - (ord(char)- 65) % 26 + 65)
            # print("Hellow")
        elif (char.islower()):
            text += chr(25 - (ord(char)- 97) % 26 + 97)
            # print("Hellw")
        else:
            text += char
    return text

def shift(Text):
    text = ""
    for char in Text:
        if (char.isupper()):
            text += chr((ord(char)- 65 + 1) % 26 + 65)
            # print("Hellow")
        elif (char.islower()):
            text += chr((ord(char)- 97 + 1) % 26 + 97)
            # print("Hellw")
        else:
            text += char
    return text

if __name__ == '__main__':
    print(decode())
   

