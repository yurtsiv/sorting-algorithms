import math
from library_sort_helpers import *

def library_sort(array, epsilon):
    init_len = math.floor((1+epsilon)*len(array))
    final_len = init_len
    rounds = math.floor(math.log2(len(array)))
    ins_in_round = 1
    for i in range(0, rounds):
        final_len += min(
            (2+2*epsilon) * ins_in_round,
            (1+epsilon) * final_len
        )
        ins_in_round *= 2


    sorted_res = [None] * int(final_len)
    insert_in_round = 1
    current_pos = 0
    end_index = math.floor((1+epsilon)*len(array))


    while current_pos < len(array):
        for _ in range(0, insert_in_round):
            print(current_pos)
            current_elem = array[current_pos]
            insert_position = find_insert_position(sorted_res, current_elem)
            
            if sorted_res[insert_position] != None:
                free_space(sorted_res, insert_position, current_elem)

            sorted_res[insert_position] = current_elem 
            current_pos += 1
            if current_pos == len(array):
                return filter_empty(sorted_res) 

        prev_end = end_index
        end_index = int(min(
            (2+2*epsilon) * insert_in_round,
            (1+epsilon) * end_index
        ))

        rebalance(sorted_res, end_index, prev_end) 
        insert_in_round *= 2

    return filter_empty(sorted_res)