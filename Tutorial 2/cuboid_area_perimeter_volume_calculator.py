#cuboid area, perimeter, volume calculator

#User input
length = float(input("Input length Using Cuboid: "))
width = float(input("Input width Using Cuboid: "))
height = float(input("Input height Using Cuboid: "))

#calculate the area(Maths: A = 2lw + 2lh + 2wh)
area = 2*length*width + 2*length*height + 2*width*height
print("The area is: ", area)

#calculate the perimeter(Maths: P = 2(l + w))
perimeter = 2*(length+width)
print("The perimeter is: ", perimeter)

#calculate the volume(Maths: V = l * w * h)
volume = length * width * height
print("The Volume is: ", volume)
