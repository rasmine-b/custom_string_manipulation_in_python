# zfill(). add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.

# Custom function to add leading zeros to a string
def custom_zfill(s, width):
    return '0' * (width - len(s)) + s if len(s) < width else s

# Get user input and prints result
