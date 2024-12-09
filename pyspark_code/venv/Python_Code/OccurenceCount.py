def output(input):
    count = 1
    out = ''
    for i in range(len(input)-1):
        if input[i] == input[i+1]:
            count += 1
        else:
            out = out + input[i] + str(count) # a1b2c2d4e2
            count  = 1
    out = out + input[i+1]+ str(count)
    return out


input = "abbccddddeeaaf"
output = output(input)
print(output) #a1b2c2d4e2a2f1
