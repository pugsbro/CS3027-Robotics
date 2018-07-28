#!/usr/bin/env python 

"""
Map Listen Script

Listens to map server and inflates map producing a represntation of the map used for path planning. Written that map to a file called grid.txt

Written by Bradley Scott
Student ID:51661169
Email: b.scott.16@aberdeen



"""
import rospy 
from nav_msgs.msg import OccupancyGrid
from geometry_msgs.msg import Point
from geometry_msgs.msg import Quaternion
from std_msgs.msg import String
import json
class mapl:
	def __init__(self):
		
		rospy.init_node('maplisten', anonymous = True)
        	
		subscriber = rospy.Subscriber("/map", OccupancyGrid, self.callback)
                
	def callback(self,data):

		self.mape = OccupancyGrid()
		self.mape.data = data.data
		self.mape.info = data.info 
		print("origin is: ", self.mape.info.origin)	
		print ("width of map is", self.mape.info.width)
		print("height of map is:", self.mape.info.height)
		print("resolution of map is: ", self.mape.info.resolution)
		

		self.grid = [[0 for x in range(self.mape.info.width)] for y in range(self.mape.info.height)]
		self.inflatedGrid = [[0 for x in range(self.mape.info.width)] for y in range(self.mape.info.height)]
	
		i = 0
		inflation = 15
		for y in range(0,self.mape.info.height):
			for x in range(0,self.mape.info.width):
				if (self.mape.data[i]!= 0):
					#self.grid[y][x] = [1]
					for yy in range(-inflation,inflation):
						for xx in range(-inflation,inflation):
							if y+yy<0 or x+xx<0 or y+yy>=self.mape.info.height or x+xx>=self.mape.info.width:
								continue
							self.inflatedGrid[y+yy][x+xx] = 1
				i += 1

		
		with open("grid.txt", "w") as outfile:
			json.dump(self.inflatedGrid,outfile)
		
		
		
		print ("map representation and inflation complete")

		

"""
origin + index(pq path values) * resolution 
"""

mapr = mapl()
rospy.spin()





