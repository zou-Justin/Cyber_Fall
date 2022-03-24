def read():
    with open('temp.txt','wb') as file:
        array = [65,66,97,98,10,72,101,108,108,111,32,119,111,114,108,100,10]
        for i in array:
            a = i.to_bytes(len(array), byteorder='big')
            file.write(a)

def write():
    with open('temp.txt','rb') as fileR, open("test2.txt", 'wb') as outfile:
        for i in fileR.read():
            a = int.from_bytes(i,byteorder='big')
            print(a)
            c = a.to_bytes(17,byteorder='big')
            outfile.write(c)

read()
write()