


def merge_intervals(intervals):
    
    final  = [intervals[0]]
    
    
    for item in intervals[1:]:
        print(item, item[1],final[-1][-1])
        
        if  item[0] > final[-1][-1]:
            final.append(item )
        else:
            final [-1][-1] = item [1]
    return final
        
        
        



intervals = [[1, 4], [2, 5], [6, 7], [8, 10]]
print(merge_intervals(intervals))
