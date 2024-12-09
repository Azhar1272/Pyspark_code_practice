# count of word

def countofelement(s):
    lst = []
    lst = s.split(' ')
    distinct_list = set(lst)
    dic = {}
    for x in distinct_list:
        dic.update({x:lst.count(x)})
    return dic

s = "hello world hello"
output = countofelement(s)
print(output) #{'world': 1, 'hello': 2}