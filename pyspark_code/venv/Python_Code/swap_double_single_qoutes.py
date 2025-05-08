def swap_quotes(s: str) -> str:
    """
    Swaps all double quotes with single quotes and vice versa in the given string.
    """
    placeholder = '__TEMP__'
    return s.replace('"', placeholder).replace("'", '"').replace(placeholder, "'")

# Example usage:
example = '"Hello", it\'s me.'
print(swap_quotes(example))  # Output: "'Hello', it\"s me."
