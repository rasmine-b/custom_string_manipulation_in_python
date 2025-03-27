# lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

# Convert uppercase letters (A-Z) to lowercase (a-z) manually
def custom_lower(s):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':  
            result += chr(ord(char) + 32)  
        else:
            result += char
    return result

# Get user input and prints result
text = input("Enter a string: ")
print(f"Modified: {custom_lower(text)}")