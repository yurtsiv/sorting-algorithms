import math

def merge(left, right):
    result = []
    left_pointer = right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right): 
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1

    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])

    return result

def merge_sort(array):
    arr_len = len(array)

    if arr_len == 1:
        return array

    mid_index = math.floor(arr_len / 2)

    left_sorted = merge_sort(array[:mid_index])
    right_sorted = merge_sort(array[mid_index:])

    return merge(left_sorted, right_sorted)