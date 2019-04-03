import math
from library_sort_helpers import *

def library_sort(array, epsilon):
    sorted_res = [None] * math.floor((1+epsilon)*len(array))
    insert_in_round = 1
    current_pos = 0
    while current_pos < len(array):
        for i in range(0,insert_in_round):
            insert_position = find_insert_position(sorted_res, array[current_pos])
            if sorted_res[insert_position] != None:
                free_space(sorted_res, insert_position)

            sorted_res[insert_position] = array[current_pos]
            current_pos += 1

            if current_pos > len(array):
                return [e for e in sorted_res if e != None]
    
        rebalance(sorted_res)
        insert_in_round *= 2

    return [e for e in sorted_res if e != None]