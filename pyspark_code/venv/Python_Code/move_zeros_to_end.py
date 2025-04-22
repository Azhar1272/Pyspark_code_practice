"""
Problem: Move all zeros in the list to the end while preserving the order of other elements.
"""

input_list = [7, 2, 0, 34, 56, 12, 0, 5, 6, 8, 0, 0, 9, 0, 1, 2, 4, 5]
zero = []
non_zero = []

for x in input_list:
    if x == 0:
        zero.append(x)
    else:
        non_zero.append(x)

final = non_zero + zero
print("Output:", final)
