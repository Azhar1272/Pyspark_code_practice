def merge_intervals(intervals):
    # Sort intervals by the start time
    intervals.sort()
    
    # Initialize merged list with the first interval
    merged = [intervals[0]]
    print(merged)
    print(intervals[1:])
    for start, end in intervals[1:]:
        print(start,end)
        
        # If there's overlap, merge intervals
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
            print(merged)
        else:
            # No overlap, add a new interval
            merged.append([start, end])
    
    return merged

# Example usage
intervals = [[1, 3], [2, 5], [7, 9], [8, 10]]
result = merge_intervals(intervals)
# print("Merged intervals:", result)

