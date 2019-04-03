import math
from stack import Stack

def partition(arr,start,end): 
    pivot_index = start 
    pivot = arr[end] 
  
    for i in range(start, end):
        if arr[i] <= pivot: 
            arr[pivot_index],arr[i] = arr[i],arr[pivot_index] 
            pivot_index += 1 

    arr[pivot_index],arr[end] = arr[end],arr[pivot_index] 
    return pivot_index 


def quick_sort_iterative(arr): 
    start = 0
    end = len(arr) - 1

    stack = Stack(len(arr)) 
    
    stack.push(start)
    stack.push(end)
  
    while not stack.is_empty(): 
        end = stack.pop()
        start = stack.pop()
  
        pivot_index = partition(arr, start, end) 
  
        if pivot_index-1 > start: 
            stack.push(start)
            stack.push(pivot_index - 1)

        if pivot_index+1 < end: 
            stack.push(pivot_index + 1)
            stack.push(end)