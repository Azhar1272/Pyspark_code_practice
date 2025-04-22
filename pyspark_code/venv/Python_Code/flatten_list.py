"""
Problem: Flatten a nested list.
"""

a = [1, [2, 4], [2, [4, 6]]]
final = []

def flatlist(a):
    for x in a:
        if not isinstance(x, list):
            final.append(x)
        else:
            flatlist(x)
    return final

print("Flattened List:", flatlist(a))  

#[1, 2, 4, 2, 4, 6]

