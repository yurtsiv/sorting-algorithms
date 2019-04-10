def quick_sort(array):
  if len(array) == 1 or len(array) == 0:
    return array

  pivot_index = len(array) // 2
  pivot, rest = array[pivot_index], array[pivot_index+1:]
  left = [e for e in rest if e <= pivot]
  right = [e for e in rest if e > pivot]
  left_sorted = quick_sort(left)
  right_sorted = quick_sort(right)

  return left_sorted + [pivot] + right_sorted 