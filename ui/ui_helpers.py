import math

from simulation import SequenceTypes

def get_int(label, min, max):
  res = None

  while res == None:
    entered = input(label + "(from " + str(min) + " to " + str(max) + "):")
    try:
      parsed = int(entered)
      if parsed >= min and parsed <= max:
        return parsed
      else:
        print("From " + str(min) + " to " + str(max) + " !")
    except ValueError:
      print("Enter an integer") 

def get_gaps_sequence(_):
  result = []

  print("\nEnter gaps sequence in descending order (the last gap should be 1):")
  init_gap = get_int("", 1, math.inf)
  result.append(init_gap)

  while result[-1] != 1:
    next_gap = get_int("", 1, result[-1] - 1)
    result.append(next_gap)

  return result

def get_bucket_size(arr):
  return get_int("\nBucket size", 1, len(arr)) 

def get_shrink_factor(arr):
  return get_int("\nShrink factor", 1.1, len(arr))

def get_seq_len():
  return get_int("\nSequence length", 10, 2000000)

def get_seq_type():
  types_titles = list(map(lambda t: t.name, SequenceTypes))
  for i in range(0, len(types_titles)):
    print(str(i) + ") " + types_titles[i])
  
  selected_option = get_int("\nChoose sequence type", 0, len(types_titles) - 1)
  selected_type = types_titles[selected_option]
  return SequenceTypes[selected_type]

  


