#copy and paste the alice frequency value and hard code it in
import sys
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
                if alphabet[k] == i.lower(): 
                    dict[alphabet[k]] += 1;  
    return dict



def EuclidianDistance(fileName, baseFile):
    distance = 0
    value = list(Read(fileName).values())
    total = sum(Read(fileName).values())
    value2 = list(Read(baseFile).values())
    total2 = sum(Read(baseFile).values())
    for i in range(len(value)):
        distance += (((value[i]/total) - (value2[i]/total2)) ** 2)
    return math.sqrt(distance)

def decode(Caesar_text):
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
# up to 16 length
def guessKeyLength(fileName):
    pass


def Decypher(fileName):
    file = open(fileName,'r')
    Length = 1
    fileText = file.read()
    piles = [""] * Length
    strName = "Pile"
    finalText = ""
    actualFinalText = ""
    minimumDistance = 0
    Decode = ""
    for j in range(16):
        for i in range(len(fileText)):
            for k in range(Length):
                if i % Length == k:
                    piles[i%Length] += fileText[i]
        for i in range(Length):
            Pile1 = open(strName + str(i),'w')
            Decode = decode(Pile1)
            for i in range(len(Decode)):
                finalText += decode[i % Length][i / Length]
        pile23 = open('newText.txt','w')
        pile23.write(finalText)
        pile23.close()
        dist = EuclidianDistance('newText.txt',"temp.txt")
        if (dist < minimumDistance):
            minimumDistance = dist
            p = open('newText.txt','r')
            actualFinalText = p.read()
            finalText = ""
        Length+=1
    return actualFinalText

if __name__ == '__main__':
    print(Decypher("temp2.txt"))