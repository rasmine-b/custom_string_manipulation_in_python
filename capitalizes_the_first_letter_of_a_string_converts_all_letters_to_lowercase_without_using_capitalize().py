# capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

# Returns the string with the first letter capitalized and the rest in lowercase
def custom_capitalize(s):
    if not s:
        return s 
    
    first_char = s[0]  
    remaining_chars = s[1:]  
    return (chr(ord(first_char) - 32) if 'a' <= first_char <= 'z' else first_char) + remaining_chars.lower()

# Get user input and prints result
