# endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

# Checks and returns True if the string ends with the given suffix; otherwise, returns False
def custom_endswith(s, suffix):
    return s[-len(suffix):] == suffix if len(suffix) <= len(s) else False

# Get user input and prints result
