def output(fl):
    dic = {}
    cnt = 0
    for lst in fl:
        for item in lst:
            if item in dic:
                #cnt = dic[item] + len(lst)-1
                #dic.update({item:cnt})
                 dic[item] += len(lst)-1 
            else:
                dic.update({item:len(lst)-1})
    return dic

fl = [[1,2,3], [2,3,1,4], [4,3]]
print(output(fl)) #{1: 5, 2: 5, 3: 6, 4: 4}


'''
#Another way to do this 

def output(fl):
    
    final = {}
    
    for item in fl:
        for x in item:
            
            final[x] = final.get(x,0)+len(item)-1
            
    return final 

''
