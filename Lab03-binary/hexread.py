def hexFile(fileName):
    hexcode = ""
    with open('test.txt','r') as file:
        for i in file.read():
          hexcode += hex(ord(i)) + " "
    return hexcode


print(hexFile('test.txt'))
