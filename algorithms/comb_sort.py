def comb_sort(array, shrink_factor):
    if shrink_factor <= 1:
        raise Exception('shring factor should be > 1')

    gap = len(array)
    is_sorted = False

    while not is_sorted:
        gap = gap // shrink_factor
        if gap <= 1:
            gap = 1
            is_sorted = True

        for i in range(0, len(array) - gap):
            if array[i+gap] < array[i]:
                temp = array[i]
                array[i] = array[i+gap]
                array[i+gap] = temp
                is_sorted = False

    return array 
