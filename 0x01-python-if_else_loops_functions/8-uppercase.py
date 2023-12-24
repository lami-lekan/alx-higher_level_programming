#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            letter = 32
        else:
            letter = 0
        print("{}".format(chr(ord(str[i])-letter)), end='')
    print()
