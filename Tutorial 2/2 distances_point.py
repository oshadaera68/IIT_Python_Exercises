#Distance Between 2 points

#importing math module
import math

#user inputs
x1 = int(input("Enter Point 1: "))
x2 = int(input("Enter Point 2: "))
y1 = int(input("Enter Point 3: "))
y2 = int(input("Enter Point 4: "))

#calculation of the distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("(x1, y1),(x2, y2) distance is: ", distance) 
