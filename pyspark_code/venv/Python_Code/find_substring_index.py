""Solution (without using built-in functions):"""

def find_substring(s: str, sub: str) -> int:
    # If both string and substring are empty, return 0
    if s == "" and sub == "":
        return 0
    
    # If substring is empty, return 0 (empty substring is always found at index 0)
    if sub == "":
        return 0
    
    # Iterate through the string `s` and check for the substring `sub`
    for i in range(len(s) - len(sub) + 1):
        # Check if the substring matches
        if s[i:i+len(sub)] == sub:
            return i  # Return the starting index
    return -1  # Return -1 if substring is not found

# Example usage
s = "hello world"
sub = "world"
output = find_substring(s, sub)
print(output)

##using built in funtion 

def find_substring(s: str, sub: str) -> int:
    # If both string and substring are empty, return 0
    if s == "" and sub == "":
        return 0
    # Use the find method to locate the substring
    return s.find(sub)

# Example usage
s = "hello world"
sub = "world"
output = find_substring(s, sub)
print(output)

