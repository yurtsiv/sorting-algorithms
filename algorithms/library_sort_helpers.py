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
            for i in range(middle_index, end + 1):
                if array[i] != None:
                    middle_non_empty_index = i
                    break

            if middle_non_empty_index == None:
                for i in range(middle_index, start - 1, -1):
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

    if end < 0:
        return 0
    elif start >= len(array):
        return len(array) - 1

    return start

def free_space(array, index, elem):
    shift_right = False
    for i in range(index, len(array)):
        if array[i] != None and array[i] > elem:
            break

        if array[i] == None:
            shift_right = True
            break
    
    pointer = index
    next_elem = array[index]

    while next_elem != None:
        if shift_right:
            tmp = array[pointer+1]
            array[pointer+1] = next_elem
            next_elem = tmp
            pointer += 1
        else:
            tmp = array[pointer-1]
            array[pointer-1] = next_elem
            next_elem = tmp
            pointer -= 1

    
    array[index] = None

def rebalance(array, end_index, prev_end_index):
    gap_size = len(array) // prev_end_index 
    insert_index = len(array) - 1
    elems_to_move = (end_index - prev_end_index) / gap_size
    
    for i in range(prev_end_index - 1, 0, -1):
        if elems_to_move == 0:
            break
        
        if i != insert_index and array[i] != None:
            array[insert_index] = array[i]
            array[i] = None
            insert_index -= gap_size 
            elems_to_move -= 1


def filter_empty(array):
    return [e for e in array if e != None]
