#!/usr/bin/python
import math
import sys
import random

slugs = {
    ftl : "Fort Laramie",
    vc : "Virginia City",
    sp : "South Pass",
    slc : "Salt Lake City",
    fh : "Fort Hall",
    pdx : "Portland"
    }

# (("Fort Laramie", "Virginia City"), ("Fort Laramie", "South Pass", "Salt Lake City", "Fort Hall"), "Portland")


class City:
    def __init__(self):
        self.dests = ()

ftl, vc, sp, slc, fh = (City(), City(), City(), City(), City())


ftl.dests = (vc, sp)
vc.dests = (vc, sp)
sp.dests = (vc, sp)
slc.dests = (vc, sp)
fh.dests = (vc, sp)
