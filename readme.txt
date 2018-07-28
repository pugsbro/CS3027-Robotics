PLEASE NOTE: i used ros distro lunar for my implementation

please run source devel/setup.bash for each new terminal window opened.

TO RUN 

1. in terminal: roslaunch assessment.launch 

2. in terminal: rosrun robotics maplisten.py

3. Once maplisten prints complete.

	in terminal: rosrun robotics pathplanning.py

4. once pathplanning script completes:

  in terminal: rviz
	make sure fixed frame is set to map
	
	add 4 marker array topics with the following topics:
	goals
	realpos
	locpos
	path


5.in terminal: rosrun robotics robotmarkers.py
	amcl is displayed as a red marker(loc pos)
	
	base_pose_ground_truth is displayed as a green marker(realpos)

6. in terminal: rosrun pathmarkers.py 

	
