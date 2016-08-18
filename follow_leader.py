import turtle
import math
import random

#head directly for 'fish' most directly in their line of vision
#take a fish. iterate through all other fish,
#	1.eliminate all fish out of field of vision
#	2.choose fish most closely aligned with our heading
#	3. change our heading to go towards this fish

iterations = 100
wn = turtle.Screen()
wn.tracer(10)
wn_y = wn.window_height()
wn_x  = wn.window_width()
num_fish = 25
list_fish = [turtle.Turtle() for i in range(num_fish)]
for i in list_fish:
	i.up()
	i.setpos(random.randrange(-wn_x // 4, wn_x // 4), random.randrange(-wn_y // 4, wn_y // 4))
	i.setheading(random.randrange(360))
	#i.down()

#(Real Real -> Real)
#input d_x, d_y, get angle relative to hor line
#relative to main point
def get_angle(d_x, d_y):
	#d_sep = math.sqrt(d_x**2 + d_y**2)
	if d_x > 0 and d_y > 0:
		return math.degrees(math.atan(d_y / d_x))
	elif d_x < 0 and d_y > 0:
		return math.degrees(math.atan(d_y / d_x)) + 180
	elif d_x < 0 and d_y < 0:
		return math.degrees(math.atan(d_y / d_x)) + 180
	elif d_x > 0 and d_y < 0:
		return math.degrees(math.atan(d_y / d_x)) + 360
	
def get_nearest_heading(turt):
	min_angle = 999
	for i in list_fish:
		if i != turt:
			delta_x = i.xcor() - turt.xcor()
			delta_y = i.ycor() - turt.ycor()
			angle_i = float(get_angle(delta_x, delta_y))
			angle_diff = abs(angle_i - turt.heading())
			if angle_diff < min_angle:
				min_angle = angle_i
	return min_angle

while iterations > 1:
	new_heading = []
	for i in list_fish:
		i.setheading(get_nearest_heading(i))
	for i in list_fish:
		i.forward(10)	
			
turtle.exitonclick()
#Q: why is this not smooth?
#A: use tracer()
#Q: why am i getting type errors sometimes? 
#A: I have no idea
#NOTE: fixe code so that if noone in front, keep going straight
