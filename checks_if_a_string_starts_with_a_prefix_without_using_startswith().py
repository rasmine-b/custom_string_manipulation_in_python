# startswith(). check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.

# Checks and returns True if the string ends with the given prefix; otherwise, returns False
def custom_startswith(s, prefix):
    return s[:len(prefix)] == prefix if len(prefix) <= len(s) else False

# Get user input and prints result
text = input("Enter a string: ")
prefix = input("Enter the prefix to check: ")

if custom_startswith(text, prefix):
    print("The string starts with the given prefix.")
else:
    print("The string does NOT start with the given prefix.")
