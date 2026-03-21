def merge_sort(array):
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]
    
    # Recursion
    merge_sort(left_part)
    merge_sort(right_part)

    left_array_index = 0 # Help keep track of index
    right_array_index = 0 # Help keep track of index
    sorted_index = 0 # Help keep track of index
    
    # Assign elements to the sorted array
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index +=1