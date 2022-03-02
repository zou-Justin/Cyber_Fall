from email.mime import base
from frequency import Read
import math
import sys

def EuclidianDistance(fileName = sys.argv[1], baseFile = sys.argv[2]):
    distance = 0
    value = list(Read(fileName).values())
    total = sum(Read(fileName).values())
    value2 = list(Read(baseFile).values())
    total2 = sum(Read(baseFile).values())
    for i in range(len(value)):
        distance += (((value[i]/total) - (value2[i]/total2)) ** 2)
    return math.sqrt(distance)

if __name__ == '__main__':
    print(EuclidianDistance(sys.argv[1],sys.argv[2]))