# ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

# Returns the string with spaces added at the end to match the specified width
def custom_ljust(s, width):
    return s + ' ' * (width - len(s)) if len(s) < width else s

# Get user input and prints result
text = input("Enter a string: ")
width = int(input("Enter the desired width: "))
print(f"Modified: {custom_ljust(text, width)}")
