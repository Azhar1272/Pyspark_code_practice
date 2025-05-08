def is_palindrome(s: str) -> bool:
    """
    Checks if the provided string is a palindrome, ignoring case, spaces, and punctuation.
    """
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

# Example usage:
test_strings = [
    "madam",
    "racecar",
    "hello",
    "level",
    "world",
    "A man, a plan, a canal - Panama"
]
