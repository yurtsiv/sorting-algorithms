def selection_sort(array):
  result = [None] * len(array)
  unsorted = array[:]

  for i in range(0, len(array)):
    unsorted_min = min(unsorted)
    result[i] = unsorted_min
    unsorted.remove(unsorted_min)

  return result