from turtle import Turtle, Screen
from oop_follow_leader import Schooler
from angle_average import angle_average

class FocalFish(Schooler):
	swarm = []
	repulse = 20
	neighborhood = 100
	
	def __init__(self):
		Schooler.__init__(self)
	
	def getNewHeading(self):
		dist = []
		dist_bracket = 50
		local_swarm_heading = []
		local_swarm_towards = []
		#local_swarm_dist = []
		min_dist = 10*100000
		for other in swarm:
			dist_to_other = self.distance(other)
			dist.append(dist_to_other)
			if other != self:
				if dist_to_other < min_dist:
					min_dist = dist_to_other
						
		if min_dist < repulse:
			self.newHead = self.heading() + 50
		
		elif min_dist <= neighborhood:
			for i in range(len(dist)):
				if swarm[i] != self:
					if dist[i] < neighborhood:
						local_swarm_heading.append(swarm[i].heading())
						local_swarm_towards.append(self.towards(swarm[i]))
						#local_swarm_dist.append(self.distance(swarm[i]))
			
			align_heading = angle_average(self.heading(), local_swarm_heading)
			cohese_heading = angle_average(self.heading(), local_swarm_towards)
			self.newHead = angle_average(self.heading(), [align_heading, cohese_heading])
		
		elif min_dist > neighborhood:
			for i in range(len(dist)):
				if swarm[i] != self:
					if dist[i] < min_dist + dist_bracket:
						local_swarm_heading.append(swarm[i].heading())
						local_swarm_towards.append(self.towards(swarm[i]))
						#local_swarm_dist.append(self.distance(swarm[i]))
			
			align_heading = angle_average(self.heading(), local_swarm_heading)
			#cohese_heading = angle_average(self.heading(), local_swarm_towards)
			self.newHead = align_heading #angle_average(self.heading(), [align_heading, cohese_heading])		
	
	def setHeadingAndMove(self):
		Schooler.setHeadingAndMove()
		

def main():
	swarm_size = 25
	win = Screen()
	win.setworldcoordinates(-1000,-800,1000,800)
	win.tracer(15)
	
	for i in range(swarm_size):
		FocalFish()
	for turn in range(1000):
		for fish in FocalFish.swarm:
			fish.getNewHeading()

		for fish in FocalFish.swarm:
			fish.setHeadingAndMove()
	
	#win.exitonclick()
	
main()