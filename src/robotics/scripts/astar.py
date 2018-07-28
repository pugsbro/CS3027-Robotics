#!/usr/bin/env python

"""
A* Implementation 

Written by Bradley Scott
Student ID:51661169
Email: b.scott.16@aberdeen



"""
import heapq
import json
import math 


stuff = open('grid.txt','r')
world = json.loads(stuff.read())


size = [0,0]
size[0]=float(len(world[0]))
size[1]=float(len(world))

class astar():
		def __init__(self,start,goal):
			self.start = start
			self.goal = goal
			self.hits = []
			


		def plan(self):

		    self.pq = []
		    heapq.heappush(self.pq,(0,[self.start]))

		  

		    while (len(self.pq) > 0):
			self.bestItem = heapq.heappop(self.pq)[:]
			self.currentpath = self.bestItem[1]
			self.heur = self.bestItem[0]

			self.currentposition = self.currentpath[-1]
		 
			#print("Pos: %s, heur: %s" % (self.currentposition,self.heur));

			if (self.currentposition==self.goal):
			    # finished
			    break

			if self.currentposition in self.hits:
			    continue

			self.hits.append(self.currentposition)
	

			for n in self.neighbours(self.currentposition):
			    if n in self.hits:
				continue

			    self.newPath=self.currentpath[:]
			    self.newPath.append(n)
			    self.heur=(len(self.newPath)/100) + self.heuristic(n)*1.001
			    heapq.heappush(self.pq,((self.heur,self.newPath)))

			#heapq.heapify(pq)

		    if (len(self.pq)==0):
			print('couldnt find a path');
			pass
		    else:
			print("Done!")
			
			return [self.pq[0][1],len(self.pq[0][1])]

		def neighbours(self,coords):
		    self.x = coords[0]
		    self.y = coords[1]
		    self.maxx = size[0]
		    self.maxy = size[1]
		    self.n=[]
		    for i in range (-1,2):
			for j in range(-1,2):
			    if ((i==0 and j==0) or (i==-1 and j==-1) or (i==-1 and j==1) or (i==1 and j==-1) or (i==1 and j==1)):
			   # if ((i==0 and j==0)):
			     continue
			    else:
				xx = self.x + i
				yy = self.y + j

				if (xx >= 0 and yy >= 0):
				    if (xx < self.maxx):
				        if (yy < self.maxy):
				            if (world[yy][xx]!=0):
				                continue

					    
					    self.n.append([xx,yy])
		    return self.n

		def heuristic(self,n):



			#euclidean distance
		    dx = abs(n[0] - self.goal[0])
		    dy = abs(n[1] - self.goal[1])
		  
		    return math.sqrt(dx * dx + dy * dy)



