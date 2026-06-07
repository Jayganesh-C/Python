def merge_intervals(intervals):

    if not intervals:
        return []
    
    # Sort the intervals by the start value
    intervals.sort(key=lambda x: x[0])

    # Add the first value to the final result
    merged = [intervals[0]]

    for current in intervals[1:]:

        last_merged_end = merged[-1][1]

        # If current interval overlaps
        if current[0] < last_merged_end: 
            merged[-1][1] = max(last_merged_end, current[1]) #max is used in case intervals = [[1, 10], [2, 5]]
        else: #just append
            merged.append(current)
    return merged
    

print(merge_intervals([[1,3],[2,6],[9,10]]))