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

ftl, vc, sp, slc, fh, pdx = (City("Fort Laramie", "She had a lot of questions about the American Fur Company."),
                             City("Virginia City", "She wanted to see the birthplace of Calamity Jane."),
                             City("South Pass", "She said she was fixin' to cross the Continental Divide!"),
                             City("Salt Lake City", "She said she was planning on having coffee with the Prophet... I didn't have the heart to tell her."),
                             City("Fort Hall", "She asked about the Snake River country."),
                             City("Portland", "She said she longed to see the future home of Open Source Bridge."))

# Clue wit by Leonard. Thank you @leonardr.

ftl.dests = (vc, sp)
vc.dests = (ftl,)
sp.dests = (slc, fh)
slc.dests = (fh,)
fh.dests = (pdx,)

player = Person("none", ftl)
carmen = Person("Carmen Sandiego", pdx)
followher = "You follow Carmen to "

player.name = raw_input('What is your name? ')

print carmen.name + " has stolen a wagon tongue and we must catch her!"
print "You are in " + player.location.name + " and, after some asking around, you have learned that she sounded interested in " + carmen.location.clue + "."

print "Your choices are:"

def where2go():
    for i,x in enumerate(player.location.dests):
        print str(i+1) + ". "+ x.name

where2go()

choice = raw_input('Which way to go? ')

def choose(path):
    if int(path) not in range(1, (len(player.location.dests)+1)):
        return "That doesn't make sense, " + player.name + ", so you stay in " + player.location.name + "."
    else:
        path = int(path)
        player.location = player.location.dests[path-1]
        return followher + player.location.name

print choose(choice)

def wincondition():
    if player.location == carmen.location:
        print "You win!"
        sys.exit()

def latterchoices():
	print player.name + ", you are now in " + player.location.name + " and you can head to:"
	where2go()
	choice = raw_input('OK, now which way? ')
	print choose(choice)

while player.location !=carmen.location:
    latterchoices()
    wincondition()
