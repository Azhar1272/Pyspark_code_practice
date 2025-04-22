def find_number(s,t):
    out = []
    final = []
    for x in s:
        if target - x in s and x not in out:
            out.append(x)
            out.append(target - x)
            final.append([x, target - x])
    return final

source = [2,3,4,9,8,6,1]
target = 5
out = find_number(source, target)
print(out)



'' Another way ''
# Problem description:
# Given a list and a target sum, return a list of indices where the sum of the elements at those indices is equal to the target.

# Function code:
def find_indices(input_list, target):
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if input_list[i] + input_list[j] == target:
                return [i, j]

input_list = [1, 5, 3, 6]
target = 8
# Function call and print output:
print(find_indices(input_list, target))  # Expected output: [1, 2]

