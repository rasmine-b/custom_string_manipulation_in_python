# rindex(). return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.

# Custom function to find the last occurrence of a character in a string
def custom_rindex(s, char):
    for i in range(len(s) - 1, -1, -1):
        if s[i] == char:
            return i
    raise ValueError(f"'{char}' not found in string")

# Get user input and prints result
string = input("Enter a string: ")
character = input("Enter the character to find: ")
try:
    position = custom_rindex(string, character)
    print(f"The last occurrence of '{character}' is at index {position}.")
except ValueError as e:
    print(e)

