def is_palindrome(num):
    # Convert the integer to a string
    num_str = str(num)
    
    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]

# Example usage
print(is_palindrome(125))
# Output: True

print(is_palindrome(12345))
# Output: False
