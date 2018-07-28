#!/usr/bin/env python

"""
Path smoothing script that produces new path with fewer nodes, only including nodes which represent a change in direction.

Written by Bradley Scott
Student ID:51661169
Email: b.scott.16@aberdeen



"""
def smooth(path):
	def relativeDistance(current,node):
		return (node[0]-current[0],node[1]-current[1])

	p1prev = (0,0)
	p2prev = (0,0)
	newpath = []
	for n in range(0,len(path),2):
    		current = path[n][:]

    		if n+1>len(path)-1 or n+2>len(path)-1:
        		if n+1==len(path)-1:
            			newpath.append(path[n+1][:])
        		break

    		p1 = path[n+1]
    		p2 = path[n+2]

    		p1dist = relativeDistance(current,p1[:])
    		p2dist = relativeDistance(current,p2[:])

    		if (p1dist == p1prev and p2dist == p2prev):
        		#print('skip')
        		pass
    		else:
			#print('important: %s' % current)
			newpath.append(current)

		p1prev = p1dist
		p2prev = p2dist

	return newpath
