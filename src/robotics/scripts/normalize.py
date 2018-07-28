#!/usr/bin/env python

"""
Normalization script used throughout project to convert between stage and grid coordinates 
 
Written by Bradley Scott
Student ID:51661169
Email: b.scott.16@aberdeen



"""

def convtostage(each):
	x = each[0]
	y = each[1]
	x = -6.0 + x * 0.012000000104308128
	y =  -4.8 + y * 0.012000000104308128
	#print x,y
	return [x,y]

def convtogrid(coords):
	x = coords[0]
	y = coords[1]

	bx = -6.0
	by = -4.8
	r = 0.012000000104308128


	cx = int((x - bx)/r)
	cy = int((y - by)/r)

	return [cx,cy]
