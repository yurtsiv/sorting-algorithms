import math

def merge(arr1, arr2):
    result = []
    smaller_len = min(len(arr1), len(arr2))
    while len(arr1) != 0 and len(arr2) != 0:
        if arr1[0] < arr2[0]:
            result.append(arr1[0])
            arr1.pop(0)
        else:
            result.append(arr2[0])
            arr2.pop(0)

    for elem in arr1:
        result.append(elem)

    for elem in arr2:
        result.append(elem)

    return result

def merge_sort(array):
    arr_len = len(array)

    if arr_len == 1:
        return array

    mid_index = math.floor(arr_len / 2)

    left_sorted = merge_sort(array[:mid_index])
    right_sorted = merge_sort(array[mid_index:])

    return merge(left_sorted, right_sorted)