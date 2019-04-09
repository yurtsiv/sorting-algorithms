import math

def get_final_arr_len(unsorted_arr, epsilon):
    init_len = math.floor((1+epsilon)*len(unsorted_arr))
    final_len = init_len

    insert_in_round = 1

    rounds = math.floor(math.log2(len(unsorted_arr)))
    for _ in range(0, rounds):
        final_len += min(
            (2+2*epsilon) * insert_in_round,
            (1+epsilon) * final_len
        )

        insert_in_round *= 2

    return int(final_len)

def find_insert_position(array, elem, end_index):
    start = 0
    end = end_index

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
    elif start >= end_index:
        return end_index

    return end

def free_space(array, index, elem, end_index):
    shift_right = False
    for i in range(index, end_index + 1):
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
    gap_size = 3
    insert_index = end_index
    elems_to_move = int((end_index - prev_end_index) / gap_size)
    
    for i in range(prev_end_index, 0, -1):
        if elems_to_move == 0:
            break
        
        if i != insert_index and array[i] != None:
            array[insert_index] = array[i]
            array[i] = None
            insert_index -= gap_size 
            elems_to_move -= 1


def filter_empty(array):
    return [e for e in array if e != None]
