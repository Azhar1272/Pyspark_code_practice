def anagram(input):
    dic = {}
    for word in input:
        # Sort the word to get the key
        sorted_word = ''.join(sorted(word))
        
        # If the sorted word is already in the dictionary, append the word to the list
        if sorted_word in dic:
            dic[sorted_word].append(word)
        else:
            # If not, create a new list with the current word
            dic[sorted_word] = [word]
    
    # Convert the dictionary values (which are lists of anagrams) into a list of lists
    result = list(dic.values())
    
    # Sort each group and return the sorted anagram groups
    for group in result:
        group.sort()
    
    return result

# Example usage
input_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = anagram(input_words)
print(output)  #[['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]


''' another way :

def anagram(input):
    d = {}
    result = []
    
    for word in input:
        
        sorted_word = "".join( sorted(word))
        
        if not sorted_word in d:
            d[sorted_word] =[]
        
        d[sorted_word].append(word)
    
    return list(d.values())

# Example usage
input_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = anagram(input_words)
print(output)  #[['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]

'''


