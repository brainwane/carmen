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

ftl, vc, sp, slc, fh, pdx = (City("Fort Laramie", "she had a lot of questions about the American Fur Company."),
                             City("Virginia City", "she wanted to see the birthplace of Calamity Jane."),
                             City("South Pass", "she said she was fixin' to cross the Continental Divide!"),
                             City("Salt Lake City", "she said she was planning on having coffee with the Prophet... I didn't have the heart to tell her."),
                             City("Fort Hall", "she asked about the Snake River country."),
                             City("Portland", "she said she longed to see the future home of Open Source Bridge, the yearly conference by the Stumptown Syndicate."))

# Clue wit by Leonard. Thank you @leonardr.

ftl.dests = (vc, sp)
vc.dests = (ftl,)
sp.dests = (ftl, slc, fh)
slc.dests = (sp, fh)
fh.dests = (sp, slc, pdx)
pdx.dests = (fh,)

player = Person("none", ftl)
carmen = Person("Carmen Sandiego", random.choice((vc, sp, slc, fh, pdx)))
followher = "You follow Carmen to "

def where2go():
    for i,x in enumerate(player.location.dests):
        print str(i+1) + ". "+ x.name

def wincondition():
    if player.location == carmen.location:
        print "You found her in " + carmen.location.name + " so you win!"
        sys.exit()

def choose(path):
    try:
        int(path)
    except ValueError:
        print "That doesn't make sense, " + player.name + ", so you stay in " + player.location.name + "."
        return
    if int(path) not in range(1, (len(player.location.dests)+1)):
        return "That doesn't make sense, " + player.name + ", so you stay in " + player.location.name + "."
    else:
        path = int(path)
        player.location = player.location.dests[path-1]
        wincondition()
        carmen.location = random.choice(carmen.location.dests)
        return followher + player.location.name

def playturn():
	print player.name + ", you are now in " + player.location.name + " and you can head to:"
	where2go()
	print "You ask around about Carmen and learn that " + carmen.location.clue
	choice = raw_input('OK, now which way will you go? ')
	choose(choice)

player.name = raw_input('What is your name? ')
print "Okay, " + player.name + ", welcome to " + player.location.name + "."
print carmen.name + " has stolen a wagon tongue and we must catch her!"

while player.location !=carmen.location:
    playturn()

