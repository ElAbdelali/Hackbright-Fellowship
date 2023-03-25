# Write a program that will compute the area of a rectangle. Prompt the user to enter the width and height of the rectangle. Print a nice message with the answer.

rectangle_width = int(input("Enter the rectangle's width: "))
rectangle_height = int(input("Enter the rectangle's height: "))

rectangle_area = rectangle_height * rectangle_width

print("The rectangle's area is:", rectangle_area)