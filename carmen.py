#!/usr/bin/python
import math
import sys
import random

class City(object):
    def __init__(self, name, clue):
        self.dests = ()
        self.name = name
        self.clue = clue

class Person(object):
    def __init__(self, name, location):
        self.name = name
        self.location = location

ftl, vc, sp, slc, fh, pdx = (City("Fort Laramie", "Matthew Shepard"),
                             City("Virginia City", "a city in Montana named after an eastern State"),
                             City("South Pass", "a town named South you have to go north to get to"),
                             City("Salt Lake City", "Brigham Young"), 
                             City("Fort Hall", "Hilary Mantel"),
                             City("Portland", "the home of Open Source Bridge"))

ftl.dests = (vc, sp)
vc.dests = ()
sp.dests = (slc, fh)
slc.dests = (fh,)
fh.dests = (pdx,)

player = Person("none", ftl)
carmen = Person("Carmen Sandiego", pdx)
followher = "You follow Carmen to "

player.name = raw_input('What is your name? ')

print [x.name for x in player.location.dests]

print carmen.name + " has stolen a wagon tongue and we must catch her! Your choices are:"
for i,x in enumerate(player.location.dests):
    print x.name + " is choice #" + str(i+1)

choice = raw_input('Which way to go? ')

def firstchoice(path):
    path = int(path)
    if path not in range(1, (len(player.location.dests)+1)):
        return "That doesn't make sense, " + player.name + ", so you stay in " + player.location.name + "."
    else:
        player.location = player.location.dests[path-1]
        return followher + player.location.name

print firstchoice(choice)

if player.location == carmen.location:
    print "you win!"

print "You are now in " + player.location.name

# def chooseatrail(thecity, listoftrails):
#    for item in listoftrails:
#        if thecity == item:
#            return listoftrails.index(city)

