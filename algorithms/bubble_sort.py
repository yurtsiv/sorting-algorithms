def bubble_sort(array):
  swapped = True

  while swapped:
    swapped = False
    for index in range(0, len(array) - 1):
      if array[index] > array[index+1]:
        temp = array[index]
        array[index] = array[index+1]
        array[index+1] = temp
        swapped = True
  
  return array