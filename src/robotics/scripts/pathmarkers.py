#!/usr/bin/env python

"""
Script used to draw goals and path in rviz. 

Written by Bradley Scott
Student ID:51661169
Email: b.scott.16@aberdeen



"""

from normalize import *
import rospy
from visualization_msgs.msg import MarkerArray
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point
import json
rospy.init_node('pathlines', anonymous=True)

class cubes:
	def __init__(self):
		
		self.pub=self.pub=rospy.Publisher("/goals",MarkerArray,queue_size=200)
		self.id=8
		rospy.sleep(1)
		self.MarkerArray=MarkerArray()
		self.Line1=Marker()
		self.Line1.color.r=0
		self.Line1.color.b=1
		self.Line1.color.g=0
		self.Line1.color.a=1
		
		self.Line1.scale.x=0.2
		self.Line1.scale.y=0.2
		self.Line1.scale.z=0.2
		
		self.Line1.type=6	
		self.Line1.action=0
		self.Line1.header.frame_id="/map"
		self.Line1.id=self.id
		
		
		self.send()
	
	def add(self,x,y):
		
		

		Point1=Point(x,y,0)
		
		self.Line1.points.append(Point1)
		
		
		
		
		

	def send(self):
		self.MarkerArray.markers.append(self.Line1)
		self.pub.publish(self.MarkerArray)



class Line:
	def __init__(self):
		self.pub=self.pub=rospy.Publisher("/path",MarkerArray,queue_size=200)
		self.id=5
		rospy.sleep(1)
		self.MarkerArray=MarkerArray()
		self.Line1=Marker()
		self.Line1.color.r=1
		self.Line1.color.b=0
		self.Line1.color.g=0
		self.Line1.color.a=1
		
		self.Line1.scale.x=0.1
		self.Line1.scale.y=0.1
		self.Line1.scale.z=0.1
		
		self.Line1.type=4
		self.Line1.action=0
		self.Line1.header.frame_id="/map"
		self.Line1.id=self.id
		
		
		self.send()
	
	def add(self,x,y):
		
		

		Point1=Point(x,y,0)
		
		self.Line1.points.append(Point1)
		
		
		
		
		

	def send(self):
		self.MarkerArray.markers.append(self.Line1)
		self.pub.publish(self.MarkerArray)




goals = [[99,99],[333,233],[708,54],[875,108],[287,660]]
newgoals = []
for each in goals:
	newgoals.append(convtostage(each))
	

#print newgoals
#print goals

c=cubes()


for each in newgoals:
	c.add(each[0],each[1])
c.send()


l=Line()

pathfile = open('path.txt','r')
path = json.loads(pathfile.read())
print path

for each in path:
	#print "ADDING"
	l.add(each[0],each[1])
	#rospy.Rate(1).sleep()
l.send()
rospy.spin()
