import sys
import string


def encode():
    Alphabet = string.ascii_uppercase
    dict = {}
    for i in Alphabet:
        dict[i] = ord(i) - 65
    print(dict)
encode()