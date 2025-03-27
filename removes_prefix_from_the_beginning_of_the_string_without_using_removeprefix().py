# removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

# If the string starts with the given prefix, remove it; otherwise, return the original string
def custom_removeprefix(s, prefix):
    if s[:len(prefix)] == prefix:
        return s[len(prefix):]
    return s 
# Get user input and prints result