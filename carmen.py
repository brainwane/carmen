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
import textwrap
import mock

def anykey():
    x = raw_input("Press Return to continue. ") + "a"

class City(object):
    def __init__(self, n, c):
        self.dests = []
        self.name = n
        self.clue = c

class Villain(object):
    def __init__(self):
        self.name = random.choice(["Carmen", "Waldo", "Edward Snowden", "Lyra"])
        self.location = random.choice([fkn, chmr, ftl])

class Hero(object):
    def __init__(self):
        self.location = ind
        self.name = raw_input("Detective at keyboard, identify yourself: ")

class Game():
    def __init__(self):
        self.player = Hero()
        self.nemesis = Villain()
        
    def wincondition(self):
        return self.player.location == self.nemesis.location

    def playturn(self):
        print "%s, you are now in %s and you can head to:" % (self.player.name, self.player.location.name)
        self.where2go()
        print "You ask around about %s and learn that %s" % (self.nemesis.name, self.nemesis.location.clue)
        choice = raw_input('OK, now which way will you go? Choose a number. ')
        self.choose(choice)
        self.wincondition()
    
    def wingame(self):
		print "You found her in %s so you win!" % currentsession.nemesis.location.name
		playagain=raw_input('Would you like to play again? Y/N: ')
		if (playagain == "N") or (playagain == "n"):
			sys.exit()
		else:
			self.player.location = ind
			self.nemesis = Villain()
			print "Get ready for a new game!"
                        anykey()
			
    def where2go(self):
        for i,x in enumerate(self.player.location.dests):
            print "%d. %s" % (i+1, x.name)

    def choose(self, path):
        try:
            path = int(path)
        except ValueError:
            print "That doesn't make sense, %s, because it's not the number for one of your possible destinations." % self.player.name
            print "So you stay in %s." % self.player.location.name
            return
        if path < 1 or path > (len(self.player.location.dests)):
            return "That doesn't make sense, %s, so you stay in %s." % (self.player.name, self.player.location.name)
        else:
            self.player.location = self.player.location.dests[path-1]
            if self.wincondition(): self.wingame()
            self.nemesis.location = random.choice(self.nemesis.location.dests)
            return "You follow %s to %s." % (self.nemesis.name, self.player.location.name)

ind = City("Independence", "she thought she'd stock up for a journey -- bullets, yokes of oxen, and whatnot.")
sjo = City("Saint Joseph", "she had a headache and needed to find some baby aspirin.")
cbl = City("Council Bluffs", "she knew that you can't beat City Hall, but thought another municipal body might back down more easily.")
fkn = City("Fort Kearney", "she wanted to visit the easternmost point of the Platte River Valley's natural roadway.")
chmr = City("Chimney Rock", "the tow-headed woman was tired of spelunking and wanted to try climbing.")
ftl = City("Fort Laramie", "she had a lot of questions about the American Fur Company.")
vc = City("Virginia City", "she wanted to see the birthplace of Calamity Jane.")
sp = City("South Pass", "she said she was fixin' to cross the Continental Divide!")
slc = City("Salt Lake City", "she said she was planning on having coffee with the Prophet... they didn't have the heart to tell her.")
fh = City("Fort Hall", "she asked about the Snake River country.")
pdx = City("Portland", "she said she longed to see the future home of Open Source Bridge, the yearly conference by the Stumptown Syndicate.")

# Clue wit by Leonard. Thank you @leonardr.

ind.dests = [fkn]
sjo.dests = [fkn]
cbl.dests = [fkn]
fkn.dests = [cbl, ind, ftl, sjo, vc, chmr]
chmr.dests = [fkn]
ftl.dests = [vc, sp, fkn]
vc.dests = [ftl, fkn]
sp.dests = [fh, ftl, slc]
slc.dests = [sp, fh]
fh.dests = [sp, pdx, slc]
pdx.dests = [fh]

def test_bidirectionalpaths():
    for city in [ind, sjo, cbl, fkn, chmr, ftl, vc, sp, slc, fh, pdx]:
        for dest in city.dests:
            try:
                assert city in dest.dests
            except AssertionError:
                print "bidirectional fail! City" , city.name , "was not in" , dest.name , "destinations."
                dest.dests.append(city)
                print "fixed it!" , city.name , "now in destinations for" , dest.name , "in this list:", map(lambda x: x.name,dest.dests)

test_bidirectionalpaths()

# would be good to do pathfinding

gpl = """You are now playing: 
Where On The Oregon Trail is Carmen Sandiego?
Copyright (C) 2013 Sumana Harihareswara and licensed under the GNU Public License.
This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it under certain conditions; see https://www.gnu.org/licenses/gpl.txt for details."""

if __name__=="__main__":
    print gpl
    currentsession = Game()
    currentrank = "Okay, %s, your current rank is: Carpenter.  Welcome to %s." % (currentsession.player.name, currentsession.player.location.name)
    print textwrap.fill(currentrank,70,replace_whitespace=False)
    assert currentsession.nemesis != currentsession.player
    anykey()
    print "%s has stolen a wagon tongue and Interpol has assigned you to catch her! Get ready for a chase!" % currentsession.nemesis.name

    while True:
         currentsession.playturn()
