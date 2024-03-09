#!/usr/bin/python3
'''A square class'''


class Square:
    '''Initilization of field'''

    def __init__(self, size=0):
        self.__size = size

    '''getter'''
    @property
    def size(self):
        return self.__size

    '''setter'''
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    '''Area method'''

    def area(self):
        return self.__size * self.__size
