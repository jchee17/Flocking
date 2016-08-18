#averages angles vectorally
#does not work if angles directly oppose each other
from math import cos, sin, atan, degrees, radians

def angle_average(init_heading, list_ang):
	acc_x = 0
	acc_y = 0
	
	for i in list_ang:
		i = radians(i)
		acc_x = acc_x + cos(i)
		acc_y = acc_y + sin(i)
		
	if -10**-10 <= acc_x <= 10**-10 or -10**-10 <= acc_y <= 10**-10:
		return init_heading
		
	return degrees(atan(acc_y / acc_x))

# angles = [45, 315]	
# print(angle_average(25, angles))
	