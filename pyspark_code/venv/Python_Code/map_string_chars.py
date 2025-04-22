"""
Problem: Map characters from one string to another by index, avoiding remapping already mapped characters.
"""

str1 = 'hljljq'
str2 = 'abcdef'

char_map = {}
final = ''

for k, v in zip(str1, str2):
    if k not in char_map:
        char_map[k] = v
    final += char_map[k]

print("Character Map:", char_map)
print("Mapped Output:", final)
