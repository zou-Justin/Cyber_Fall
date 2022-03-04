from frequency import Read
from distance import EuclidianDistance
import sys

#reverse alphabet is a different case from simply shifiting down by 1 so account for it
def decode(Caesar_text = sys.argv[1]):
    newText = ""
    while True:
        dist = EuclidianDistance(Caesar_text,"temp.txt")
        if (dist <= .019):
            with open(Caesar_text,'r') as file:
                newText = file.read()
            return newText
        else:
            shift(Caesar_text)

def shift(Text):
    for i in Text:
        chr(ord(i)+1)

if __name__ == '__main__':
    decode()


