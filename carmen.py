#!/usr/bin/python
import math
import sys

cities = {
        "0": "city of Butte",
        "1": "Fort Laramie",
        "2": "South Pass",
        "3": "Chimney Rock"
        }

choice = raw_input('Choose a number from 1 to 4: ')

def choosepath(path):
    path = choice
    if path == '1':
        return cities['0']
    if path == '2':
        return cities['1']
    if path == '3':
        return cities['2']
    if path == '4':
        return cities['3']
    else:
        return "hey, you did not follow the rules"

print choosepath(choice)
