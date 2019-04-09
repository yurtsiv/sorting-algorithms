import math
from library_sort_helpers import *

def library_sort(unsorted_arr, epsilon):
    sorted_res = [None] * get_final_arr_len(unsorted_arr, epsilon) 

    insert_in_round = 1
    current_elem_index = 0
    sorted_end_index = math.floor((1+epsilon) * len(unsorted_arr))

    while current_elem_index < len(unsorted_arr):
        for _ in range(0, insert_in_round):
            print(current_elem_index)
            current_elem = unsorted_arr[current_elem_index]
            insert_position = find_insert_position(sorted_res, current_elem, sorted_end_index)
            
            if sorted_res[insert_position] != None:
                free_space(sorted_res, insert_position, current_elem, sorted_end_index)

            sorted_res[insert_position] = current_elem 
            current_elem_index += 1

            if current_elem_index == len(unsorted_arr):
                return filter_empty(sorted_res) 

        prev_end = sorted_end_index
        sorted_end_index += int(min(
            (2+2*epsilon) * insert_in_round,
            (1+epsilon) * prev_end
        )) - 1

        rebalance(sorted_res, sorted_end_index, prev_end) 
        insert_in_round *= 2

    return filter_empty(sorted_res)