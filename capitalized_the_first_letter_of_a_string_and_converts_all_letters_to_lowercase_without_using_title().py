# title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

# Returns a string where each word starts with an uppercase letter and the rest are lowercase
def custom_title(s):
    words = s.split() 
    result = []

    for word in words:
        if word:  
            first_char = word[0]  
            remaining_chars = word[1:] 

            new_word = (chr(ord(first_char) - 32) if 'a' <= first_char <= 'z' else first_char) + remaining_chars.lower()
            result.append(new_word)
    
    return ' '.join(result)  

# Get user input and prints result
