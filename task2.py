#ask the user to enter the shape we will be calculating to area for
from turtle import width


shape = input("what shape is the building between a square, rectangle and a circle: ")

#calculate the different shapes in order to get the area of the buliding
if shape == "square":
    lenght = int(input("What is the lenght of the building: "))
    square = lenght ** 2
    print(square)
elif shape == "rectangle":
    lenght = int(input("Enter the lenght of the building: "))
    width = int(input("Enter the width of the building: "))
    rectangle = lenght * width
    print(rectangle)
elif shape == "circle":
    radius = int(input("Enter the radius of the building: "))
    circle = 3.14 * radius ** 2
    print(circle)
else:
    print("Invalid selection")