#copy and paste the alice frequency value and hard code it in
import sys
import string
import math
import os

def Read(fileName):
    alphabet = list(string.ascii_lowercase)
    dict = {}
    for k in range(26):
        dict[alphabet[k]] = 0
    for i in fileName:
        if i.isupper() or i.islower():
            dict[i.lower()] += 1;  
    total = sum(dict.values())
    for i in range(26):
        dict[alphabet[i]] = dict[alphabet[i]]/total; 
    return dict

def EuclidianDistance(fileName, baseFile):
    distance = 0
    alphabet = list(string.ascii_lowercase)
    value = Read(fileName)
    value2 = Read(baseFile)
    for i in alphabet:
        distance += ((value[i] - value2[i]) ** 2)
    return math.sqrt(distance)

def readAlice(temp):
    file = open(temp,'r')
    text = ""
    for i in file.read():
        text += i
    return text

a = readAlice("temp.txt")

def h(Caesar_text):
    newText = ""
    file = ""
    minimumDistance = 1000
    shiftedText = ""
    for i in range(26):
        dist = EuclidianDistance(Caesar_text,a)
        if (dist < minimumDistance):
            minimumDistance = dist
            newText = Caesar_text
        shiftedText = shift(Caesar_text)
        Caesar_text = shiftedText
    # shiftedText = reverseShift(Caesar_text)
    # Caesar_text = shiftedText
    # for i in range(26):
    #     dist = EuclidianDistance(Caesar_text,a)
    #     if (dist < minimumDistance):
    #         minimumDistance = dist
    #         newText = Caesar_text
    #     shiftedText = shift(Caesar_text)
    #     Caesar_text = shiftedText
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
    Length = 5
    fileText = file.read()
    file.close()
    strName = "Pile"
    finalText = ""
    actualFinalText = ""
    minimumDistance = 1
    Decode = ""
    # for j in range(5):
    piles = [""] * Length
    for i in range(len(fileText)):
        if i % Length == 0:
                piles[i%Length] += fileText[i]
        elif i % Length == 1:
                piles[i%Length] += fileText[i]
        elif i % Length == 2:
                piles[i%Length] += fileText[i]
        elif i % Length == 3:
                piles[i%Length] += fileText[i]
        elif i % Length == 4:
                piles[i%Length] += fileText[i]
        # elif i % Length == 0:
        #         piles[i%Length] += fileText[i]
        
        # for k in range(Length):
    print(piles[0])
    for i in range(Length):
        Pile1 = piles[i]
        Decode = h(Pile1)
        print(Decode + "  hello")
    #     Pile1 = open(strName + str(i),'w')
    #     Pile1.truncate()
    #     Pile1.write(Decode)
    #     Pile1.close()
    # for i in range(len(fileText)):
    #     p = open(strName + str(i % Length))
    #     finalText += p.read()[i//Length]
    # pile23 = open('newText.txt','w')
    # pile23.write(finalText)
    # pile23.close()
    # print(finalText)
    # dist = EuclidianDistance('newText.txt',"temp.txt")
    # if (dist <= 0.05):
    #     minimumDistance = dist
    #     p = open('newText.txt','r')
    #     actualFinalText = p.read()
    #     p.close()
    # finalText = ""
    # #Length+=1
    # return actualFinalText

if __name__ == '__main__':
    # Read('hello darkness')
    #print(Decypher("temp2.txt"))
    print(h('Jmqi rhybbyw, qdt jxu ibyjxo jelui. Tyt wohu qdt wycrbu yd jxu mqru: Qbb cycio muhu jxu rehewelui, Qdt jxu cecu hqjxi ekjwhqru'))