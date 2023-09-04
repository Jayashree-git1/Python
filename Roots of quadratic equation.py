# Defining Function To Find Roots
def findRoots(a, b, c):    
    d = (b*b - 4*a*c)**0.5    
    x1 = (-b + d)/(2*a)    
    x2 = (-b - d)/(2*a)    
print('\nROOTS OF GIVEN QUADRATIC EQUATIONS ARE:')    
print('x1: {0}'.format(x1))    
print('x2: {0}'.format(x2))
# Input Section
print('Solving ax^2 + bx + c =0')
a = float(input('Enter the value of a: '))
b = float(input('Enter the value of b: '))
c = float(input('Enter the value of c: '))
# Function Call
findRoots(a,b,c)