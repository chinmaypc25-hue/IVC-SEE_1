def reverse_string(s):
    """
    Reverse a string using Python's slice notation.
    
    Args:
        s (str): The string to reverse
        
    Returns:
        str: The reversed string
    """
    return s[::-1]


def reverse_string_loop(s):
    """
    Reverse a string using a loop.
    
    Args:
        s (str): The string to reverse
        
    Returns:
        str: The reversed string
    """
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


# Example usage
if __name__ == "__main__":
    text = "Hello, World!"
    
    print(f"Original string: {text}")
    print(f"Reversed (slice): {reverse_string(text)}")
    print(f"Reversed (loop): {reverse_string_loop(text)}")
