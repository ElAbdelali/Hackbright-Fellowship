# Using Python comment syntax (prepend the line with a #) at the bottom of your repl.it session answer the following question:

# Why is the following Python invalid?

# first_name = "Sally"
# first_name[0] = "C"

first_name = "Sally"
#first_name[0] = "C"


# The reason the above is invalid is because strings are immutable, meaning they can't change.

# Instead, we can create a new string with the modified value by concatenating the new char with the rest of the string as follows: 

second_name = "C" + first_name[1:]
print(second_name)