#!/usr/bin/env python 

"""
Script for displaying robot markers in rviz. 
There are two markers, one displaying the robots actual position using base pose ground truth and another using amcl localization.


Written by Bradley Scott
Student ID:51661169
Email: b.scott.16@aberdeen



"""

import rospy 
from geometry_msgs.msg import PointStamped  
from visualization_msgs.msg import MarkerArray
from visualization_msgs.msg import Marker
from std_msgs.msg import Header 
import tf 
from geometry_msgs.msg import Point
from geometry_msgs.msg import *
from nav_msgs.msg import Odometry
from normalize import *
rospy.init_node('testlinez', anonymous=True)
class cubes:
	def __init__(self):
		#no queue to update on each movement
		
		self.pub=self.pub=rospy.Publisher("/realpos",MarkerArray,queue_size=100)
		
		self.id=3
		self.MarkerArray=MarkerArray()
		self.Cube=Marker()
		self.Cube.color.r=0
		self.Cube.color.b=0
		self.Cube.color.g=1
		self.Cube.color.a=1
		
		self.Cube.scale.x=0.1
		self.Cube.scale.y=0.1
		self.Cube.scale.z=0.2
		self.Cube.ns = "base"
		self.Cube.type=1	
		self.Cube.action=0
		self.Cube.header.frame_id="/map"
		self.Cube.id=self.id
	
	def add(self,position,orientation):

		self.pose1=Pose(position,orientation)
		
		self.Cube.pose = self.pose1
		
		
		
		
		

	def send(self):
		#print(self.Cube.pose)
		self.MarkerArray.markers.append(self.Cube)
		self.pub.publish(self.MarkerArray)


class cube2:
	def __init__(self):
		#no queue to update on each movement
		self.pub=self.pub=rospy.Publisher("/locpos",MarkerArray,queue_size=100)
		
		self.id=1
		self.MarkerArray=MarkerArray()
		self.Cube=Marker()
		self.Cube.color.r=1
		self.Cube.color.b=0
		self.Cube.color.g=0

		self.Cube.color.a=1
		
		self.Cube.scale.x=0.1
		self.Cube.scale.y=0.1
		self.Cube.scale.z=0.2
		self.Cube.ns = "fake localization"
		self.Cube.type=1	
		self.Cube.action=0
		self.Cube.header.frame_id="/map"
		self.Cube.id=self.id
	
	def add(self,position,orientation):
		
		

		self.pose1=Pose(position,orientation)
		
		self.Cube.pose = self.pose1
		
		
		
		
		

	def send(self):
		self.MarkerArray.markers.append(self.Cube)
		self.pub.publish(self.MarkerArray)




def realpos(data): 
	#print("where i really really am (base ground truth)")
	#print data
	reals = data
	
	#rospy.loginfo(rospy.get_caller_id() + "I heard %s", data) 
	#base pos is where you really are
	position=reals.pose.pose.position
	orientation=reals.pose.pose.orientation

	cb = cubes()
	cb.add(position,orientation)
	cb.send()
	
 
def flocal(data): 
	#print("fake localization")
	#print data
	#rospy.loginfo(rospy.get_caller_id() + "I heard %s", data) 
	#base pos is where you really are	
	fakes = data
	pub=rospy.Publisher("/localizationtask",PoseWithCovarianceStamped,queue_size=0)
 	pub.publish(data)
	position=fakes.pose.pose.position
	orientation=fakes.pose.pose.orientation
	c = cube2()
	c.add(position,orientation)
	c.send()



		
	


def listener():
	
	
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		#amcl instead 
		rate.sleep()

  		
		try:
			rospy.Subscriber("/base_pose_ground_truth", Odometry, realpos)
		except Exception as e:
			pass
		#where it thinks it is 

		try:
                	rospy.Subscriber("/amcl_pose", PoseWithCovarianceStamped, flocal) 
		except Exception as e:
			pass
		
		rospy.spin()



if __name__ == '__main__': 

	listener() 
