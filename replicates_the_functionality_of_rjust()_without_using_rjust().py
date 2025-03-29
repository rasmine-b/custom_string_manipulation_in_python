# rjust(). add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.

# Returns the string with spaces added at the end to match the specified width
def custom_rjust(s, width):
    return ' ' * (width - len(s)) + s if len(s) < width else s

# Get user input and prints result