def max_val(input):
    max_val = 0
    max_key =''
    for key in input:
        if input[key] > max_val:
            max_val = input[key]
            max_key = key
    return max_key
