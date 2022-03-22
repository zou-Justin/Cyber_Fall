def read():
    with open('temp.txt','wb') as file:
        array = [65,66,97,98,10,72,101,108,108,111,32,119,111,114,108,100,10]
        for i in array:
            print(i)
            a = i.to_bytes(len(array), byteorder='big')
            file.write(a)

def write():
    with open('temp.txt','rb') as fileR:
        for i in fileR.read():
            print(i)
            # a = int.from_bytes(i,byteorder='big')
            # a+=1
            # c = a.to_bytes(17,byteorder='big')
            # fileW.write(c)

# read()
write()