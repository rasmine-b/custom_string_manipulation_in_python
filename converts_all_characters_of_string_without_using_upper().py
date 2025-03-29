# upper(). converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.

# Convert lowercase letters (a-z) to uppercase (A-Z) manually
def custom_upper(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

# Get user input and prints result
text = input("Enter a string: ")
print(f"Modified: {custom_upper(text)}")

