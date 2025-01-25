# list[start:stop:step]
# index start from 0
# len gives you number of elements
# Negative indexing gives elements reverse and start from -1

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(lst[2:6])  # [2, 3, 4, 5]
print(lst[:5])   # [0, 1, 2, 3, 4] (start from index 0)
print(lst[5:])   # [5, 6, 7, 8, 9] (stop at last element)
print(lst[1:8:2])  # [1, 3, 5, 7] (every 2nd element from index 1 to 7)
print(lst[::3])    # [0, 3, 6, 9] (every 3rd element)
print(lst[-5:-1])  # [5, 6, 7, 8] (5th last to 2nd last)
print(lst[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reverses the list)
print(lst[::-2])  # [9, 7, 5, 3, 1] (every 2nd element in reverse)
lst[2:5] = ['a', 'b', 'c'] # Modifying Elements Using Slicing
print(lst)  # [0, 1, 'a', 'b', 'c', 5, 6, 7, 8, 9]
