def is_sorted(array):
  min = array[0]
  for elem in array:
    if elem < min:
      return False
  return True

def bubble_sort(array):
  result = array[:]
  while not is_sorted(result):
    for index in range(0, len(result) - 1):
      if result[index] > result[index+1]:
        temp = result[index]
        result[index] = result[index+1]
        result[index+1] = temp
  return result