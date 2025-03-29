# index(). return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.

# Custom function to find the first occurrence of a character in a string
def custom_index(s, char):
    for i in range(len(s)):
        if s[i] == char:
            return i
    raise ValueError(f"'{char}' not found in string")

# Get user input and prints result