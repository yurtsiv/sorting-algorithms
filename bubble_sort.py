def is_sorted(array):
  min = array[0]
  for elem in array:
    if elem < min:
      return False
  return True

def bubble_sort(array):
  while not is_sorted(array):
    for index in range(0, len(array) - 1):
      if array[index] > array[index+1]:
        temp = array[index]
        array[index] = array[index+1]
        array[index+1] = temp
