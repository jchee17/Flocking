from turtle import Turtle, Screen
from oop_follow_leader import Schooler
from angle_average import angle_average

class FocalFish(Schooler):
	swarm = []
	repulse = 20
	neighborhood = 100
	
	off_course = 30
	dist_bound = 50
	
	def __init__(self):
		Schooler.__init__(self)
	
	def getMinAndDist(self):
		list_dist = []
		min_dist = self.distance(swarm[0])
		
		for other in swarm:
			dist_to_other = self.distance(other)
			list_dist.append(dist_to_other)
			if other != self:
				if dist_to_other < min_dist:
					min_dist = dist_to_other
		
		return(list_dist, min_dist)
	
	def getNewHeading(self):
		temp = getMinAndDist(self)
		list_dist = temp[0]
		min_dist = temp[1]
		local_swarm_heading = []
		local_swarm_towards = []
		
		if min_dist < repulse:
			self.newHead = self.heading() + off_course
			
		elif min_dist <= neighborhood:
			for i in range(len(dist)):
				if swarm[i] != self:
					if list_dist[i] < neighborhood:
						local_swarm_heading.append(swarm[i].heading())
						local_swarm_towards.append(self.towards(swarm[i]))
			
			new_heading = angle_average(local_swarm_heading, local_swarm_towards)
			self.NewHead = new_heading
		
		elif min_dist > neighborhood:
			for i in range(len(dist)):
				if swarm[i] != self:
					if dist[i] < min_dist + dist_bound:
						local_swarm_heading.append(swarm[i].heading())
						local_swarm_towards.append(self.towards(swarm[i]))
			new_heading = angle_average(local_swarm_heading, local_swarm_towards)
			self.NewHead = new_heading		
	
	def setHeadingAndMove(self):
		Schooler.setHeadingAndMove()
		

def main():
	swarm_size = 25
	win = Screen()
	win.setworldcoordinates(-1000,-800,1000,800)
	win.tracer(15)
	
	for i in range(swarm_size):
		FocalFish()
	for turn in range():
		for fish in FocalFish.swarm:
			fish.getNewHeading()

		for fish in FocalFish.swarm:
			fish.setHeadingAndMove()
	
	#win.exitonclick()
	
main()