import math

def comb_sort(array, shrink_factor):
    if shrink_factor < 1:
        raise Exception('shring factor should be >= 1')

    result = array[:]
    gap = len(result)
    is_sorted = False

    while not is_sorted:
        gap = math.floor(gap / shrink_factor)
        if gap <= 1:
            gap = 1
            is_sorted = True

        for i in range(0, len(result) - gap):
            if result[i+gap] < result[i]:
                temp = result[i]
                result[i] = result[i+gap]
                result[i+gap] = temp
                is_sorted = False

    return result 