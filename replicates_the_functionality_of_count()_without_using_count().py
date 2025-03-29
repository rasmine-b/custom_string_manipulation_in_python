# count(). return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

# Function to count how many times a substring appears in a string
def custom_count(s, sub):
    return sum(1 for i in range(len(s) - len(sub) + 1) if s[i:i+len(sub)] == sub)

# Get user input and prints result
