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

