def xorDecode(fileName,keyFile):
    with open(fileName,'rb') as file1,open(keyFile,'rb') as file2,open(keyFile,'wb') as file3:
        file = file1.read()
        key = file2.read()
        for i in range(len(file1.read())):
            a = (file[i] ^ key[i % len(key.read())])
        file3.write(a)
    
xorDecode("test2.txt","output.txt")