def shell_sort(arr, gaps):
  result = arr[:]
  for gap in gaps:
    for i in range(gap,len(arr)): 
      # add a[i] to the elements that have been gap sorted 
      # save a[i] in temp and make a hole at position i 
      temp = result[i] 

      # shift earlier gap-sorted elements up until the correct 
      # location for a[i] is found 
      j = i 
      while  j >= gap and result[j-gap] > temp: 
          result[j] = result[j-gap] 
          j -= gap 

      # put temp (the original a[i]) in its correct location 
      result[j] = temp 
  
  return result
