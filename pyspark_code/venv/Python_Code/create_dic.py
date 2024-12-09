# create dic from given input
def create_dic(keys,values):
    dic = {}
    for i in range(len(keys)):
        dic[keys[i]] = values[i]
    return dic


keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

output = create_dic(keys,values)
print(output) # {'name': 'Alice', 'age': 25, 'city': 'New York'}