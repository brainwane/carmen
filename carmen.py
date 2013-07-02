#!/usr/bin/python
import math
import sys
import random

cities = {
        "0": "Fort Laramie, Wyoming",
        "1": "South Pass, Wyoming",
        "2": "Virginia City, Montana",
        "3": "Fort Hall, Idaho",
        "4": "Salt Lake City, Utah"
        }

# time to construct the "tree" of possibilities as a dictionary of lists

trails = { 
    "Bozeman trail" : ["Fort Laramie", "Virginia City"],
    "Usual trail" : ["South Pass", {
        "Mormon trail" : ["Salt Lake City" , "Fort Hall"],
        "Gentile trail" : "Fort Hall"
        },
        "Portland"]
    }

currentcity = "Fort Laramie"

carmencity = cities[str(random.randrange(0,4))]

username = raw_input('What is your name? ')

print "You are in " + currentcity

choice = raw_input('Carmen Sandiego has gone rogue! To find her lair, choose a number from 1 to 4: ')

carmenis = "You follow Carmen to "

def choosepath(path):
    path = choice
    global currentcity
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

if currentcity == carmencity:
    print "you win!"
