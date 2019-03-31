def bubble_sort(array):
  result = array[:]
  swapped = True

  while swapped:
    swapped = False
    for index in range(0, len(result) - 1):
      if result[index] > result[index+1]:
        temp = result[index]
        result[index] = result[index+1]
        result[index+1] = temp
        swapped = True

  return result