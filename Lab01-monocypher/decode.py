from turtle import distance
from frequency import Read

def decode(Caesar_text):
    dict = Read(Caesar_text)
    Dict2 = Read("temp.txt")
    shift = distance(Caesar_text,"temp.txt")
    for i in dict.values():
        print(i)
            


