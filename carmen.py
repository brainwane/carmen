#!/usr/bin/python

# Copyright 2013 Sumana Harihareswara

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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

ind, sjo, cbl, fkn, chmr = (City("Independence", "she thought she'd stock up for a journey -- bullets, yokes of oxen, and whatnot."),
                            City("Saint Joseph", "she had a headache and needed to find some baby aspirin."),
                            City("Council Bluffs", "she knew that you can't beat City Hall, but thought another municipal body might back down more easily."),
                            City("Fort Kearney", "she wanted to visit the easternmost point of the Platte River Valley's natural roadway."),
                            City("Chimney Rock", "the tow-headed woman was tired of spelunking and wanted to try climbing."))

ftl, vc, sp, slc, fh, pdx = (City("Fort Laramie", "she had a lot of questions about the American Fur Company."),
                             City("Virginia City", "she wanted to see the birthplace of Calamity Jane."),
                             City("South Pass", "she said she was fixin' to cross the Continental Divide!"),
                             City("Salt Lake City", "she said she was planning on having coffee with the Prophet... they didn't have the heart to tell her."),
                             City("Fort Hall", "she asked about the Snake River country."),
                             City("Portland", "she said she longed to see the future home of Open Source Bridge, the yearly conference by the Stumptown Syndicate."))

# Clue wit by Leonard. Thank you @leonardr.

ind.dests = (fkn,)
sjo.dests = (fkn,)
cbl.dests = (fkn,)
fkn.dests = (ind, sjo, cbl, chmr)
chmr.dests = (fkn, ftl)
ftl.dests = (vc, sp)
vc.dests = (ftl,)
sp.dests = (ftl, slc, fh)
slc.dests = (sp, fh)
fh.dests = (sp, slc, pdx)
pdx.dests = (fh,)

player = Person("none", ind)
carmen = Person("Carmen Sandiego", random.choice((fkn, chmr, ftl, vc, sp, slc, fh, pdx)))

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
        print "That doesn't make sense, " + player.name + ", because it's not the number for one of your possible destinations."
        print "So you stay in " + player.location.name + "."
        return
    if int(path) not in range(1, (len(player.location.dests)+1)):
        return "That doesn't make sense, " + player.name + ", so you stay in " + player.location.name + "."
    else:
        path = int(path)
        player.location = player.location.dests[path-1]
        wincondition()
        carmen.location = random.choice(carmen.location.dests)
        return "You follow Carmen to " + player.location.name

def playturn():
	print player.name + ", you are now in " + player.location.name + " and you can head to:"
	where2go()
	print "You ask around about Carmen and learn that " + carmen.location.clue
	choice = raw_input('OK, now which way will you go? ')
	choose(choice)
	wincondition()

print "You are now playing: Where On The Oregon Trail is Carmen Sandiego?"
player.name = raw_input('Detective at keyboard, please identify yourself: ')
print "Okay, " + player.name + ", your current rank is: Carpenter.  Welcome to " + player.location.name + "."
print carmen.name + " has stolen a wagon tongue and Interpol has assigned you to catch her! Get ready for a chase and stay on your toes, because she is on the move!"

while player.location !=carmen.location:
    playturn()

