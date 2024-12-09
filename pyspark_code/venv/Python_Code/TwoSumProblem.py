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
