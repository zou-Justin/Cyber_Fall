from frequency import Read
from distance import EuclidianDistance
import sys

#reverse alphabet is a different case from simply shifiting down by 1 so account for it
def decode(Caesar_text = sys.argv[1]):
    newText = Caesar_text
    while True:
        dist = EuclidianDistance(Caesar_text,"temp.txt")
        if (dist <= .019):
            #return something
            return "this is good"
        else:
            shift(Caesar_text)

def shift(Text):
    for i in Text:
        chr(ord(i)+1)



