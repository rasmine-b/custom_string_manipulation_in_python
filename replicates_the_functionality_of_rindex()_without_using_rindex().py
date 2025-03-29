# rindex(). return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.

# Custom function to find the last occurrence of a character in a string
def rindex(s, char):
    for i in range(len(s) - 1, -1, -1):
        if s[i] == char:
            return i
    raise ValueError(f"'{char}' not found in string")

# Get user input and prints result
