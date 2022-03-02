import string;

def Read(fileName):
    alphabet = list(string.ascii_lowercase)
    dict = {}
    counter = 0
    for k in range(26):
        dict[alphabet[k]] = 0
    with open(fileName,'r') as file:
        for i in file.read():
            for k in range(26): 
                if alphabet[k] == i: 
                    dict[alphabet[k]] += 1;  
    return dict

values = Read('temp.txt').values()
total = sum(values)
key_list = list(Read('temp.txt').keys())
val_list = list(values)
for i in range(26):
    print(key_list[i] + " " + str(val_list[i]/total))
