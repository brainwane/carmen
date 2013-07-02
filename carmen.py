#!/usr/bin/python
import math
import sys

cities = {
        "0": "city of Butte",
        "1": "Fort Laramie",
        "2": "South Pass",
        "3": "Chimney Rock"
        }

username = raw_input('What is your name? ')

choice = raw_input('Carmen Sandiego has gone rogue! To find her lair, choose a number from 1 to 4: ')

carmenis = "Carmen Sandiego is in "

def choosepath(path):
    path = choice
    if path == '1':
        return carmenis + cities['0']
    if path == '2':
        return carmenis + cities['1']
    if path == '3':
        return carmenis + cities['2']
    if path == '4':
        return carmenis + cities['3']
    else:
        return "hey, you did not follow the rules, " + username

print choosepath(choice)
