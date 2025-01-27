def is_balanced(s):
    d = {"]" :"[" , "}" : "{", ")" : "("}
    open = []

    
    for x in s:
        if x in d.values():
            open.append(x)
        elif  x in d.keys():
            if not open or open.pop() != d[x]:
                return False
    return not open

            
s = '{[]}'

print("Balanced:" if is_balanced(s) else "Not Balanced")
