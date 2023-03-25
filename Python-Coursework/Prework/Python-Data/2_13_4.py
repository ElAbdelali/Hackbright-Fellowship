# It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday. If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights you would return home on a Saturday (day 6) Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the number of day of the week you will return on.

starting_day = input("What day of the week are you leaving? (0-6): ")
vacation_days = input("How many days will you be vacationing for: ")

return_day = (int(starting_day)+(int(vacation_days)))%7

print("you will return on", return_day, "day of the week")