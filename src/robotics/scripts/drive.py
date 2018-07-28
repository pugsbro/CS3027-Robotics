#!/usr/bin/env python

"""
Ros driving node  

Written by Bradley Scott
Student ID:51661169
Email: b.scott.16@aberdeen



"""
#rosservice call /reset_positions
import rospy
from geometry_msgs.msg  import Twist
import tf 
from math import pow,atan2,sqrt
import json 
from geometry_msgs.msg import *
from nav_msgs.msg import Odometry
from time import time
rospy.init_node('driving_node', anonymous=True)

		 
stuff = open('path.txt','r')
path = json.loads(stuff.read())

class turtlebot():
 
     def __init__(self,goalx,goaly):
         #Creating our node,publisher and subscriber
	 self.goal_x = goalx
	 self.goal_y = goaly
	 self.x = None
	 self.y = None
	 self.angle = None
         
	 
	 self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=0)
      
	 rospy.wait_for_message('base_pose_ground_truth',Odometry, timeout=None)	 	 
	 self.pose_subscriber = rospy.Subscriber('base_pose_ground_truth', Odometry, self.callback)

	 self.odomrep = Odometry()
	 self.rate = rospy.Rate(5)
		



	
 
     #Callback function implementing the pose value received
     def callback(self, data):
	 #print data
	 self.odomrep.pose.pose.orientation = data.pose.pose.orientation
	 self.odomrep.pose.pose.position = data.pose.pose.position
         self.odomrep.pose.pose.position.x = round(self.odomrep.pose.pose.position.x, 2)
         self.odomrep.pose.pose.position.y = round(self.odomrep.pose.pose.position.y, 2)

	

	 self.x = self.odomrep.pose.pose.position.x
	 self.y = self.odomrep.pose.pose.position.y
	 
	
	 quaternion = (
		 self.odomrep.pose.pose.orientation.x,
		 self.odomrep.pose.pose.orientation.y,
		 self.odomrep.pose.pose.orientation.z,
		 self.odomrep.pose.pose.orientation.w)
	 euler = tf.transformations.euler_from_quaternion(quaternion)
	 self.angle = euler[2]
	 #print ("x is: ", self.x, "y is: ", self.y, "angle in radians is: ", self.angle)
	 
 
     def get_distance(self):
         self.distance = sqrt(pow((self.goal_x - self.x), 2) + pow((self.goal_y - self.y), 2))
	 print ("distnace from goal is:", self.distance)
         return (self.distance)

     def getx (self):
	return self.x

     def gety(self):
	return self.y

     def getangle(self):
	return self.angle 

     def theta(self):
	xr = self.goal_x - self.x
	yr = self.goal_y - self.y
	return atan2(yr , xr)
	

     def rotate2goal(self):
      	vel_msg = Twist()
     	speed = 0.9
     	angle = self.angle-self.theta()
     
     	while (abs(angle)>0.03):
     
     		angle = self.theta()-self.angle
     
     		#print("ROT")
     
     	     	#angular velocity in the z-axis:
     		vel_msg.angular.x = 0
     		vel_msg.angular.y = 0
     		vel_msg.angular.z = angle*speed
     
     		     #Publishing our vel_msg
     		self.velocity_publisher.publish(vel_msg)
     		self.rate.sleep()
     
     	
     	vel_msg.linear.x = 0
     	vel_msg.angular.z =0
     	self.velocity_publisher.publish(vel_msg)

     def move2goal(self):
       
         vel_msg = Twist()
	 #print goal_pose
         
         t1 = rospy.Time.now()
         t2 = rospy.Time.now()
	 print ("time is:",t1)
	 speed = 0.15

	 print(self.distance)
 
         while (((t2.to_sec() - t1.to_sec()) * speed) <= self.distance):
	
	 	t2 = rospy.Time.now()
	 
	 		
		vel_msg.linear.x = speed
		vel_msg.linear.y = 0
		vel_msg.linear.z = 0
	 

		#print("HELLO")
	 
		     #Publishing our vel_msg
		self.velocity_publisher.publish(vel_msg)
		self.rate.sleep()
        

	 #Stopping our robot after the movement is over
         vel_msg.linear.x = 0
         vel_msg.angular.z =0
         self.velocity_publisher.publish(vel_msg)
 
         
 
if __name__ == '__main__':
     	try:
		times = time()

		path=list(path[1:])
		
		for each in path:
			xxyy = (each[0],each[1])
			print("moving to point: ",xxyy[0],xxyy[1])
			x = turtlebot(xxyy[0], xxyy[1])
			rate = rospy.Rate(5)

			while(x.getx()==None or x.gety()==None):
				rate.sleep()

			d = x.get_distance()

			if (d <= 0.1):
				print ("skip goal")
				continue

			x.rotate2goal()
			x.move2goal()
			print("gets here")

		
	except rospy.ROSInterruptException:
		pass

	print ("end")
	print (time() - times)

		 
	 
