import math

def find_insert_position(array, elem):
    start = 0
    end = len(array) - 1

    while start < end:
        middle_index = math.floor((end + start) / 2)
        middle_non_empty_index = None

        if array[middle_index] != None:
            middle_non_empty_index = middle_index
        else:
            ## if middle elem is empty, find nearest non empty
            for i in range(middle_index, 0):
                if array[i] != None:
                    middle_non_empty_index = i
                    break

        if middle_non_empty_index == None:
            return middle_index
        
        middle_elem = array[middle_non_empty_index]

        if elem == middle_elem:
            return middle_non_empty_index
        elif elem < middle_elem:
            end = middle_non_empty_index - 1
        else:
            start = middle_non_empty_index + 1

    return start

def free_space(array, index):
    pointer = index
    next_elem = array[index]
    array[index] = None

    while next_elem != None:
        temp = array[pointer+1]        
        array[pointer+1] = next_elem
        next_elem = temp

def rebalance(array):
    for i in range(0, len(array) - 2):
        if array[i] != None and array[i+1] != None:
            array.insert(i + 1, None)

def filter_empty(array):
    return [e for e in array if e != None]
