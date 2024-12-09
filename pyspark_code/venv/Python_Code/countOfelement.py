# count of each element present in list

def countOfelement(lst):
    distinct_list = set(lst)
    dic = {}
    for x in distinct_list:
        dic.update({x:lst.count(x)})
    return dic



lst = ['a', 'c', 'b', 'b', 'c', 'c', 'd']
output = countOfelement(lst)
print(output) #{'d': 1, 'c': 3, 'a': 1, 'b': 2}
