# Importing math library
import math
# Reading radius and angle of polar coordinate
radius = float(input('Enter radius: '))
theta = float(input('Enter theta in degree: '))
# Converting theta from degree to radian
theta = theta * math.pi/180.0;
# Converting polar to cartesian coordinates
x = radius * math.cos(theta)
y = radius * math.sin(theta)
# Displaying cartesian coordinates
print('Cartesian coordinate is: (x = %0.2f, y = %0.2f)' %(x,y))
