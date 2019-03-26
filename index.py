from bubble_sort import bubble_sort
from selection_sort import selection_sort 
from insertion_sort import insertion_sort
from bucket_sort import bucket_sort
from merge_sort import merge_sort
from comb_sort import comb_sort
from library_sort import library_sort

arr = [5,3,2,6,7,9,0]

print("Bubble sort")
print(bubble_sort(arr))

print("Selection sort")
print(selection_sort(arr))

print("Insertion sort")
print(insertion_sort(arr))

print("Bucket sort")
print(bucket_sort(arr, 3))

print("Merge sort")
print(merge_sort(arr))

print("Comb sort")
print(comb_sort(arr, 1.3))

print("Library sort")
print(library_sort(arr, 0.5))
