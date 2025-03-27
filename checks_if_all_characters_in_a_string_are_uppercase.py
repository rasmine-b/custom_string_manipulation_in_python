# isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

# Checks and returns True if all letters in the string are uppercase; otherwise, returns False
def custom_isupper(s):
    for char in s:
        if 'a' <= char <= 'z': 
            return False
    return True

# Get user input and prints result
