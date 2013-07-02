#!/usr/bin/python
import math


choice = raw_input('Choose a number from 1 to 4: ')

def choosepath(path):
    path = choice
    if path == '1':
        return "cool, 1 is great!"
    if path == '2':
        return "you chose 2"
    if path == '3':
        return "you chose 3"
    if path == '4':
        return "you chose 4, that is weird"
    else:
        return "hey, you did not follow the rules"

print choosepath(choice)
