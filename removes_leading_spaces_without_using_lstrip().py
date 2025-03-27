# lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

# Define a function named custom_lstrip that takes a string 's' as input
def custom_lstrip(s):
    i = 0
    while i < len(s) and s[i] == ' ':
        i += 1
    return s[i:]
# Get user input and print output