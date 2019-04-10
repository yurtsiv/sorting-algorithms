def shell_sort(arr, gaps):
  for gap in gaps:
    for i in range(gap, len(arr)): 
      temp = arr[i] 

      j = i 
      while  j >= gap and arr[j-gap] > temp: 
          arr[j] = arr[j-gap] 
          j -= gap 

      arr[j] = temp 

  return arr
