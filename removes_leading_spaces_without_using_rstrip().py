# rstrip(). remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

# Define a function named custom_rstrip that takes a string 's' as input
def custom_rstrip(s):
    i = len(s) - 1
    while i >= 0 and s[i] == ' ':
        i -= 1
    return s[:i + 1]

# Get user input and prints result
