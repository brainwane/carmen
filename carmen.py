#!/usr/bin/python
import math
import sys

cities = {
        "0": "city of Butte",
        "1": "Fort Laramie",
        "2": "South Pass",
        "3": "Chimney Rock"
        }

currentcity = "Independence"

username = raw_input('What is your name? ')

print "You are in " + currentcity

choice = raw_input('Carmen Sandiego has gone rogue! To find her lair, choose a number from 1 to 4: ')

carmenis = "You follow Carmen to "

def choosepath(path):
    path = choice
    if path == '1':
        currentcity = cities['0']
        return carmenis + currentcity
    if path == '2':
        currentcity = cities['1']
        return carmenis + currentcity
    if path == '3':
        currentcity = cities['2']
        return carmenis + currentcity
    if path == '4':
        currentcity = cities['3']
        return carmenis + currentcity
    else:
        return "hey, you did not follow the rules, " + username + ", so you stay in " + currentcity

print choosepath(choice)
