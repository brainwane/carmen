#!/usr/bin/python
import math
import sys
import random

class City(object):
    def __init__(self, name):
        self.dests = ()
        self.name = name

ftl, vc, sp, slc, fh, pdx = (City("Fort Laramie"), City("Virginia City"), City("South Pass"), City("Salt Lake City"), 
                             City("Fort Hall"), City("Portland"))

ftl.dests = (vc, sp)
vc.dests = ()
sp.dests = (slc, fh)
slc.dests = (fh,)
fh.dests = (pdx,)

currentcity = ftl

# I'll be randomizing which city Carmen is in later; the "cities" dict no longer exists.
# carmencity = cities[str(random.randrange(1,len(cities)))]

carmencity = pdx

username = raw_input('What is your name? ')

print "You are in " + currentcity.name + ", and you can go to Virginia City, Montana, or South Pass, Wyoming."

print "Carmen Sandiego has stolen a wagon tongue and we must catch her!"

choice = raw_input('Which way to go? South Pass (SP) or Virginia City (VC)? ')

followher = "You follow Carmen to "

def firstchoice(path):
    path = choice
    global currentcity
    if path == 'VC':
        currentcity = "Virginia City"
        return followher + currentcity.name
    if path == 'SP':
        currentcity = "South Pass"
        return followher + currentcity.name
    else:
        return "That doesn't make sense, " + username + ", so you stay in " + currentcity.name + "."

print firstchoice(choice)

if currentcity == carmencity:
    print "you win!"

if currentcity == trails[0][1]:
    print "You are on the Bozeman trail. Wrong turn! No sign of Carmen here; time to head back."
    secondchance = raw_input('Which way to go? South Pass (SP) or Virginia City (VC)? ')
    firstchoice(secondchance)
    print firstchoice(secondchance)

# if currentcity == trails[1][1]:
#    print "You are on the right track! From here, the Mormon trail or the Gentile trail?"


# def chooseatrail(thecity, listoftrails):
#    for item in listoftrails:
#        if thecity == item:
#            return listoftrails.index(city)

