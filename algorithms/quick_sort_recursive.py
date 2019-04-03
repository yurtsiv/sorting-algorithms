def quick_sort_recursive(array):
  if len(array) == 1 or len(array) == 0:
    return array

  pivot, rest = array[0], array[1:]
  min = [e for e in rest if e <= pivot]
  max = [e for e in rest if e > pivot]
  left_sorted = quick_sort(min)
  right_sorted = quick_sort(max)

  return left_sorted + [pivot] + right_sorted 