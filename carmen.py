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
    "Usual trail" : ["Fort Laramie", "South Pass", {
        "Mormon trail" : ["Salt Lake City" , "Fort Hall"],
        "Gentile trail" : "Fort Hall"
        },
        "Portland"]
    }

currentcity = "Fort Laramie"

# I'll be randomizing which city Carmen is in later.
# carmencity = cities[str(random.randrange(1,len(cities)))]

carmencity = "Portland"

username = raw_input('What is your name? ')

print "You are in " + currentcity + ", and you can go to Virginia City, Montana, or South Pass, Wyoming."

print "Carmen Sandiego has stolen a wagon tongue and we must catch her!"

choice = raw_input('Which way to go? South Pass (SP) or Virginia City (VC)? ')

followher = "You follow Carmen to "

def choosepath(path):
    path = choice
    global currentcity
    if path == 'VC':
        currentcity = cities['1']
        return followher + currentcity
    if path == 'SP':
        currentcity = cities['2']
        return followher + currentcity
    else:
        return "That doesn't make sense, " + username + ", so you stay in " + currentcity + "."

print choosepath(choice)

if currentcity == carmencity:
    print "you win!"

print "OK, now you are in " + currentcity + "."
