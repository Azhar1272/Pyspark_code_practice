def find_first_last(nums: List[int], target: int) -> List[int]:
    try:
        first = nums.index(target)
        last = len(nums) - 1 - nums[::-1].index(target)
        return [first, last]
    except ValueError:
        return [-1, -1]

# Example usage:
print(find_first_last([1, 2, 3, 4, 5, 6, 7, 7, 7], 7))  # Output: [6, 8]
