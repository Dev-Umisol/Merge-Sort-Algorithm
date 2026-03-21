def merge_sort(array):
    # Base Case
    if len(array) <= 1:
        return
    
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
        
        sorted_index +=1 # <-- move next in the index
    
    # Left or right might still have elements in them while the other side won't i.e. left might have elements left in the group, but right might not, or vice versa
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1

if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)
    merge_sort(numbers)
    print('Sorted array: ')
    print(numbers)