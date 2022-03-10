
def Decypher(N):
    file = open('Cipher.txt','r')
    fileText = file.read()
    piles = [""] * N
    for i in range(len(fileText)):
        if i % N == 0:
            piles[i%N] += fileText[i]
        elif i % N == 1:
            piles[i%N] += fileText[i]
        elif i % N == 2:
            piles[i%N] += fileText[i]
        elif i % N == 3:
            piles[i%N] += fileText[i]
    Pile1 = open('Pil1','w')
    Pile1.write(pile1)
    Pile1.close()
    Pile2 = open('Pil2','w')
    Pile2.write(pile2)
    Pile2.close()
    Pile3 = open('Pil3','w')
    Pile3.write(pile3)
    Pile3.close()
    Pile4 = open('Pil4','w')
    Pile4.write(pile4)
    Pile4.close()
    # DecodeP1 = decode('Pil1')
    # DecodeP2 = decode('Pil2')
    # DecodeP3 = decode('Pil3')
    # DecodeP4 = decode('Pil4')
    finalText = ""
    for i in range(len(DecodeP4)):
        finalText += DecodeP1[i] + DecodeP2[i] + DecodeP3[i] + DecodeP4[i]
    return finalText