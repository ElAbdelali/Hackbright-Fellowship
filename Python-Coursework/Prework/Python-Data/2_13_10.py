# Write a program that will compute MPG for a car. Prompt the user to enter the number of miles driven and the number of gallons used. Print a nice message with the answer.

milesDriven = int(input("Enter the distance traveled in miles: "))
gallonsUsed = int(input("Enter the number of gallons used: "))

mpg = milesDriven/gallonsUsed

print("Your car gives", mpg, "MPG")