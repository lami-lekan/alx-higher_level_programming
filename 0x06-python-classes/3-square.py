#!/usr/bin/python3
'''A square class'''


class Square:
    '''Initilization of field'''

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    '''Area method'''

    def area(self):
        return self.__size * self.__size
