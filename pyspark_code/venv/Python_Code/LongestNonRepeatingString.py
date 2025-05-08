def output(s):
    out = ''
    dic = {}
    len_out = 0
    for x in s:
        if x not in out:
            out = out + x
        else:
            if len(out) > len_out:
                len_out = len(out)
                final_output = out
            out = x
    else:
        if len(out) > len_out:
                len_out = len(out)
                final_output = out
                
    return final_output       


s = "abcefabcdefghkj"
out = output(s)
print(out) #abcdefghkj


'''Another way :

def output(s):
     
     out =''
     final =''
     max = 0
     for x in s:
         
         if x not in out:
             out += x
         else:
             if max < len(out):
                 max = len(out)
                 final  = out+x
                 
             
             out = x
                 
                 
     return out
            
             
            


s = "abcefabcdefghkj"
out = output(s)
print(out) #abcdefghkj'''
