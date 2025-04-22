# Problem description:
# Given two strings, create a new string where each character from str1 is replaced by a corresponding character from str2. 
# If a character from str1 is already mapped, do not change it.

# Function code:
str1 = 'hljljq'
str2 = 'abcdef'
map = {}
final = ''

for k, v in zip(str1, str2):
    if k not in map.keys():
        map.update({k: v})
    final += map[k]

# Function call and print output:
print(map, final)  # {'h': 'a', 'l': 'b', 'j': 'c', 'q': 'f'} abcbcf
