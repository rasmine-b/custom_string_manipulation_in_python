# center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

# Returns the string centered within the given width by adding spaces on both sides
def custom_center(s, width):
    if width <= len(s):  
        return s  

    total_spaces = width - len(s)
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces  

    return ' ' * left_spaces + s + ' ' * right_spaces

# Get user input and prints result