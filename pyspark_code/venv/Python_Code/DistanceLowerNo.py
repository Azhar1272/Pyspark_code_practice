
Input = [73, 76, 72, 69, 71, 75, 74, 70]
# Output: [2, 1, 1, 0, 3, 1, 1, 0] → how far first lower number on right for each number. If not consider 0.  


    
def lowerNo(Input):
    out =[]
  
    
    for i in range(len(Input)):
        cnt = 0
        for j in range (i+1,len(Input)):
            cnt += 1
            if Input[i] > Input[j]:
                out.append(cnt)
                break
        else:
            out.append(0)
                
            
              
    return out
    
print(lowerNo(Input))
                    
