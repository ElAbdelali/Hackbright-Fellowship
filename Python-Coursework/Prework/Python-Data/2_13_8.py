# Write a program that will compute the area of a circle. Prompt the user to enter the radius and print a nice message back to the user with the answer.

pi = 3.14
radius = int(input("Enter the radius of the circle: "))
area = pi*(radius**2)

print("The area of the circle is:", area)
