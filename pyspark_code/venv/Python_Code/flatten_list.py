a = [1, [2, 4], [2, [4, 6]], {2,3}]
final = []

def flatlist(a):
    for x in a:
        if not isinstance(x, (list, set)):
            final.append(x)
        else:
            flatlist(x)
    return final

print("Flattened List:", flatlist(a))  
