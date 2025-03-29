# startswith(). check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.

# Checks and returns True if the string ends with the given prefix; otherwise, returns False
def custom_startswith(s, prefix):
    return s[:len(prefix)] == prefix if len(prefix) <= len(s) else False

# Get user input and prints result
