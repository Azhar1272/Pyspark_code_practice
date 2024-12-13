def max_val(input):
    max_val = 0
    max_key =''
    for key in input:
        if input[key] > max_val:
            max_val = input[key]
            max_key = key
    return max_key

# input = {'x': -10, 'y': -5, 'z': -20}
# output = max_val(input)
# print(output)

# math_operations.py
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b
