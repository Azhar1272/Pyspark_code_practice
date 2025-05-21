
3. Input = [1,3,2,2,3,1] — Output = [1,1,2,2,3,3] (Without using sorting or bubble sort method)



def manual_sort(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    result = []
    for key in range(min(nums), max(nums)+1):
        if key in count:
            result.extend([key] * count[key])
    return result

# Example
nums = [1, 3, 2, 2, 3, 1]
print(manual_sort(nums))  # Output: [1, 1, 2, 2, 3, 3]


##Another Way

from collections import Counter

def sort_by_frequency(nums):
    freq = Counter(nums)
    result = []
    for val in range(min(nums), max(nums)+1):
        result.extend([val] * freq[val])
    return result

# Example
nums = [1, 3, 2, 2, 3, 1]
print(sort_by_frequency(nums))  # Output: [1, 1, 2, 2, 3, 3]


