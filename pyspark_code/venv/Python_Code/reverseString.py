def reverse_string(s):
    lst = s.split(' ')
    out = ''
    for x in lst[::-1]:
        out += x + ' ' 

    return out.strip()

s = "My name is azhar"
# out = "azhar is name My"   
print(reverse_string(s))