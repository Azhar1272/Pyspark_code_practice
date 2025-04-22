# Problem description:
# Find the index of the substring in a string.

# Function code:
s = "Hello, welcome to the world of Python!"
sub = "welcome"

l = s.split(" ")

for i, x in enumerate(l):
    if x == sub:
        print(len(l[i-1]) + 1)

if sub in s:
    l2 = s.split(sub)
    print(l2)
    print(len(l2[0]))

# Function call and print output:


7
['Hello, ', ' to the world of Python!']
6
