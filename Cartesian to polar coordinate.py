# Importing math library
import math
# Reading cartesian coordinate
x = float(input('Enter value of x: '))
y = float(input('Enter value of y: '))
# Converting cartesian to polar coordinate  # Calculating radius
radius = math.sqrt( x * x + y * y )
# Calculating angle (theta) in radian
theta = math.atan(y/x)
# Converting theta from radian to degree
theta = 180 * theta/math.pi
# Displaying polar coordinates
print('Polar coordinate is: (radius = %0.2f,theta = %0.2f)' %(radius, theta))
