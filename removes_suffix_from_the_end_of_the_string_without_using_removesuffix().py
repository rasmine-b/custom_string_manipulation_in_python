# removesuffix(). remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.

# If the string starts with the given suffix, remove it; otherwise, return the original string
def custom_removesuffix(s, suffix):
    if s.endswith(suffix):
        return s[:-len(suffix)]
    return s

# Get user input and prints result
text = input("Enter a string: ")
suffix = input("Enter the suffix to remove: ")
result = custom_removesuffix(text, suffix)
print(f"Modified: {result}")