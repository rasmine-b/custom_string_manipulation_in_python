# swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

# Returns a new string where uppercase letters become lowercase and vice versa
def custom_swapcase(s):
    result = ""
    for char in s:
        if 'A' <= char <= 'Z':  
            result += chr(ord(char) + 32)  
        elif 'a' <= char <= 'z':  
            result += chr(ord(char) - 32)  
        else:
            result += char 
    return result

# Get user input and prints result
text = input("Enter a string: ")
print(f"Modified: {custom_swapcase(text)}")
