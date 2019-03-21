def insert_to_proper_place(array, elem):
  for i in range(0, len(array)):
    if elem < array[i]:
      array.insert(i, elem)
      return

  array.insert(len(array), elem)

def insertion_sort(array):
  result = []

  for elem in array:
    insert_to_proper_place(result, elem)

  return result
