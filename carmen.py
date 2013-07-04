#!/usr/bin/python
import math
import sys
import random

cities = {
        "1": "Virginia City, Montana",
        "2": "South Pass, Wyoming",
#        "3": "Fort Hall, Idaho",
#        "4": "Salt Lake City, Utah"
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

carmencity = cities[str(random.randrange(1,len(cities)))]

username = raw_input('What is your name? ')

print "You are in " + currentcity + ", and you can go to Virginia City, Montana, or South Pass, Wyoming."

choice = raw_input('Carmen Sandiego has stolen three wagon tongues and we must catch her! Which way to go? North (N) or west (W)? ')

followher = "You follow Carmen to "

def choosepath(path):
    path = choice
    global currentcity
    if path == 'N':
        currentcity = cities['1']
        return followher + currentcity
    if path == 'W':
        currentcity = cities['2']
        return followher + currentcity
    else:
        return "That doesn't make sense, " + username + ", so you stay in " + currentcity + "."

print choosepath(choice)

if currentcity == carmencity:
    print "you win!"
