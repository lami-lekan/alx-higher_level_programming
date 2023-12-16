#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lst_dgt = (-number % 10) * -1 
else:
    lst_dgt = number % 10
message = f'Last digit of {number} is {lst_dgt}'
if lst_dgt > 5:
    print(message + ' and is greater than 5')
elif lst_dgt == 0:
    print(message + ' and is 0')
elif lst_dgt < 6 and lst_dgt != 0:
    print(message + ' and is less than 6 and not 0')  
