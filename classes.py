#!/usr/bin/python
import math
import sys
import random

class City:
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



print [x.name for x in ftl.dests]
print [x.name for x in vc.dests]
print [x.name for x in sp.dests]
print [x.name for x in slc.dests]
print [x.name for x in fh.dests]
