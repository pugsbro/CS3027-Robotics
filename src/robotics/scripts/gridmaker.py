#!/usr/bin/env python

"""
Grid Maker Script that produces a png based on the grid.txt representation of the map.

Written by Bradley Scott
Student ID:51661169
Email: b.scott.16@aberdeen



"""

import png
import json
stuff = open('grid.txt','r')
world = json.loads(stuff.read()) 
filepointer = open('grid.png','wb')
Writer = png.Writer(1000,800,greyscale=True,bitdepth=1)
Writer.write(filepointer,world)

