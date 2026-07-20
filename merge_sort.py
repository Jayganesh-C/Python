def merge_sort(arr):
    # Base case
    if len(arr) <= 1:
        return arr
    
    # Divide the list
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    #sort both halves recursively
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # merge bith sorted
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    i, j = 0, 0
    left_length = len(left)
    right_length = len(right)
    # compare and push the smaller one
    while i < left_length and j < right_length:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # Append remaining
    result.extend(left[i:])
    result.extend(right[j:])

    return result


if __name__ == "__main__":
    numbers = [38, 27, 43, 3, 9, 82, 10]
    sorted_numbers = merge_sort(numbers)
    print("Original:", numbers)
    print("Sorted:  ", sorted_numbers)
