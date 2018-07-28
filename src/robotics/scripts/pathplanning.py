#!/usr/bin/env python
"""
Path planning script that solves travelling salesman problem and produces the shortest path using my A* implementation.

Written by Bradley Scott
Student ID:51661169
Email: b.scott.16@aberdeen



"""

from astar import astar
from pathsmooth import smooth
from normalize import *
import rospy
import json 
import itertools 
from time import time 


rospy.init_node('pathplanning_node', anonymous=True)
#performing astar on grid

t = time()



#pulling goals from parameter server
goals = [convtogrid(rospy.get_param('/robot_start')),convtogrid(rospy.get_param('/goal0')),convtogrid(rospy.get_param('/goal1')),convtogrid(rospy.get_param('/goal2')),convtogrid(rospy.get_param('/goal3'))]



#generating pair combinations of goals
#add 5 below to compute gap goal
combs = list(itertools.combinations([0,1,2,3,4],2))
print ("the number of combinations are as follows", len(combs))
d = {}
paths = {}


#cost of visiting each pair 
for each in combs:
	result = astar(goals[each[0]],goals[each[1]]).plan()
	paths[each] = result[0]
	d[each] = result[1]






#generating permutations of paths
#add 5 below to compute gap goal
perms = list(itertools.permutations([0,1,2,3,4]))
print ("this number of permutations are as follows",len(perms))
newperms = []

#removing reverse permutations
for each in perms:
	if (tuple(reversed(each)) not in newperms):
		newperms+=[each]

print ("this is the final number of permutations", len(newperms))

#cost of all paths
dp = {}

for nodes in range(len(newperms)):
	cost = 0
	for goal in range(0,len(newperms[nodes])-1):
		a = newperms[nodes][goal]
		b = newperms[nodes][goal+1]
		if (a>b):
			temp = a
			a = b
			b = temp
		key = (a,b)
		cost += d[key]

	dp[nodes] = cost



#get best costing path
bestpath = min(dp, key=dp.get)

#get the best path starting at goal
while (newperms[bestpath][0] != 0):
	del dp[bestpath]
	bestpath = min(dp, key=dp.get)


print ("best path is:", newperms[bestpath])

finalpath = []
#get path of best path
for i in range(len(newperms[bestpath])-1):
        
	a = newperms[bestpath][i]
	b = newperms[bestpath][i+1]

	if (a>b):
		temp = a
		a = b
		b = temp

		key = (a,b)
		finalpath += reversed(paths[key])
	else:
		key = (a,b)
		finalpath += paths[key]
	

#smoothing path 
finalpath = smooth(finalpath)


#converting from grid coordinates to stage coordinates
newresult = []
for each in finalpath:
	newresult.append(convtostage(each))


##write path to file
with open("path.txt", "w") as outfile:
			json.dump(newresult,outfile)

print ("path planning complete in: ", time() - t, " seconds")



