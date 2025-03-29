# islower(). check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

# Checks and returns True if all letters in the string are lowercase; otherwise, returns False
def custom_islower(s):
    for char in s:
        if 'A' <= char <= 'Z':
            return False
    return True

# Get user input and prints result