# check anagram in a given list

def anagram(input):
    sorted_word = ''
    dic = {}
    for word in  input:
        sorted_word = ''.join(sorted(word))
        if sorted_word in dic:
            dic[sorted_word].append(word)
        else:
            dic[sorted_word] = [word] # both are same word needs to pass in list coz it is a list
            dic.update({sorted_word:[word]}) # both are same word needs to pass in list coz it is a list
    
    return dic

input = ["eat", "tea", "dot", "car", "ate", "arc"]
output = anagram(input)
print(output) # {'aet': ['eat', 'tea', 'ate'], 'dot': ['dot'], 'acr': ['car', 'arc']}
