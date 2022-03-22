with open('temp.txt','wb') as file:
    array = [65,66,97,98,10,72,101,108,108,111,32,119,111,114,108,100,10]
    text = ""
    for i in array:
        print(i)
        a = i.to_bytes(len(array), byteorder='big')
        file.write(a)