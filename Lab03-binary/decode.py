import sys
from hexread import hexFile
from binascii import unhexlify

def xorDecode(fileName,keyFile):
    fileHex = hexFile(fileName)
    keyHex = hexFile(keyFile)
    fileBinary = ""
    keyBinary = ""
    finalText = ""
    for i in fileHex:
        if i.isalnum():
            if len(bin(int(i,16)).lstrip("0b")) == 3:
                fileBinary += "0" + bin(int(i,16)).lstrip("0b")
            elif len(bin(int(i,16)).lstrip("0b")) == 2:
                fileBinary += "00" + bin(int(i,16)).lstrip("0b")
            elif len(bin(int(i,16)).lstrip("0b")) == 1:
                fileBinary += "000" + bin(int(i,16)).lstrip("0b")
            elif len(bin(int(i,16)).lstrip("0b")) == 0:
                fileBinary += "0000" + bin(int(i,16)).lstrip("0b")
            elif len(bin(int(i,16)).lstrip("0b")) >= 4:
                fileBinary += bin(int(i,16)).lstrip("0b")
    for i in keyHex:
        if i.isalnum():
            if len(bin(int(i,16)).lstrip("0b")) == 3:
                keyBinary += "0" + bin(int(i,16)).lstrip("0b")
            elif len(bin(int(i,16)).lstrip("0b")) == 2:
                keyBinary += "00" + bin(int(i,16)).lstrip("0b")
            elif len(bin(int(i,16)).lstrip("0b")) == 1:
                keyBinary += "000" + bin(int(i,16)).lstrip("0b")
            elif len(bin(int(i,16)).lstrip("0b")) == 0:
                keyBinary += "0000" + bin(int(i,16)).lstrip("0b")
            elif len(bin(int(i,16)).lstrip("0b")) >= 4:
                keyBinary += bin(int(i,16)).lstrip("0b")
    for i in range(len(fileBinary)):
       a = int(fileBinary[i],2) ^ int(keyBinary[i % len(keyBinary)],2)
       finalText += str(a)
    f = hex(int(finalText,2))
    f = f.lstrip('0x')
    return unhexlify(f.rstrip()).decode()

if __name__ == '__main__':
    print(xorDecode(sys.argv[1],sys.argv[2]))