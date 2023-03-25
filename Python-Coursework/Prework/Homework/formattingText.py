
# 2) Formatting text

# Copy the following line of python into your repl.it session.

# paragraph = """An invitation to dinner was soon afterwards dispatched;
# and already had Mrs. Bennet planned the courses that were to do credit
# to her housekeeping, when an answer arrived which deferred it all. Mr.
# Bingley was obliged to be in town the following day, and, consequently,
# unable to accept the honour of their invitation, etc. Mrs. Bennet was
# quite disconcerted."""

# average_rating = 4.56789123

# Use string formatting to print the following (bonus points if you use f-strings instead of str.format()!):

#     The first ten characters of the variable paragraph followed by an elipsis (...)

#     The first 3 digits of the average_rating variable.

# The desired output is:

# An invitat...
# 4.57

paragraph = """An invitation to dinner was soon afterwards dispatched;
and already had Mrs. Bennet planned the courses that were to do credit
to her housekeeping, when an answer arrived which deferred it all. Mr.
Bingley was obliged to be in town the following day, and, consequently,
unable to accept the honour of their invitation, etc. Mrs. Bennet was
quite disconcerted."""

average_rating = 4.56789123

firstTen = paragraph[0:10]

print(f"{firstTen}...")
print(f'{average_rating:.2f}')