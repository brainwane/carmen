#!/usr/bin/python
import math
import sys
import random

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

# I'll be randomizing which city Carmen is in later; the "cities" dict no longer exists.
# carmencity = cities[str(random.randrange(1,len(cities)))]

carmencity = "Portland"

username = raw_input('What is your name? ')

print "You are in " + currentcity + ", and you can go to Virginia City, Montana, or South Pass, Wyoming."

print "Carmen Sandiego has stolen a wagon tongue and we must catch her!"

choice = raw_input('Which way to go? South Pass (SP) or Virginia City (VC)? ')

followher = "You follow Carmen to "

def firstchoice(path):
    path = choice
    global currentcity
    if path == 'VC':
        currentcity = "Virginia City"
        return followher + currentcity
    if path == 'SP':
        currentcity = "South Pass"
        return followher + currentcity
    else:
        return "That doesn't make sense, " + username + ", so you stay in " + currentcity + "."

print firstchoice(choice)

if currentcity == carmencity:
    print "you win!"

if currentcity == trails["Bozeman trail"][1]:
    print "You are on the Bozeman trail. Wrong turn! No sign of Carmen here; time to head back."
#    currentcity = "Fort Laramie"
#    secondchance = raw_input('Which way to go? South Pass (SP) or Virginia City (VC)? ')
#    print firstchoice(secondchance)

if currentcity == trails["Usual trail"][1]:
    print "You are on the right track! From here, the Mormon trail or the Gentile trail?"

