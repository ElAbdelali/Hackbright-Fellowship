# Asks a user to fill in some information about themselves (using input() to gather the information and assign it to variables). Use f-strings, input(), and variable assignment that you learned from this section’s readings.

# We’d like your file to ask and store the user’s answers to the following questions:

#     What’s your first name?

#     What’s your last name?

#     What’s your favorite color?

#     How many pets do you have?

# And then have it print a greeting that includes those values once they are collected.

fName = input('Tell us your first name: ')
lName = input('Tell us your last name: ')
favColor = input('Tell us your favorite color: ')
petAmt = input('Tell us how many pets you have: ')

print("""Great! So your name is {0} {1}, your favorite color is 
{2}, and you have {3} pets. Nice to meet you!""".format(fName, lName, favColor, petAmt))