from enum import Enum

from shell_sort import shell_sort 
from merge_sort import merge_sort
from quick_sort import quick_sort

algorithms = [ 
  {
    'name': 'Quick sort',
    'func': quick_sort,
    'additional_param': None
  },
  { 
    'name': 'Merge sort',
    'func': merge_sort,
    'additional_param': None
  },
  {
    'name': 'Shell sort',
    'func': shell_sort,
    'additional_param': [
      # Shell
      [1000000, 500000, 250000, 125000, 62500, 31250, 15625, 7812, 3906, 1953, 976, 488, 244, 122, 61, 30, 15, 6, 3, 2, 1],
      # Frank & Lazarus
      [1000001, 500001, 250001, 125001, 62501, 31251, 15626, 7813, 3907, 1954, 977, 489, 245, 123, 62, 31, 16, 8, 4, 2, 1],
      # Hibbard
      [4194303, 2097151, 1048575, 524287, 262143, 131071, 65535, 32767, 16383, 8191, 4095, 2047, 1023, 511, 255, 127, 63, 31, 15, 7, 3, 1]
    ]
  },
]

sequence_lengths = [100000, 500000, 1000000, 2000000]

class SequenceTypes(Enum):
  SORTED_DESCENDING = 'SORTED_DESCENDING'
  RANDOM = 'RANDOM',
  HALF_SORTED = 'HALF_SORTED',
  SORTED = 'SORTED',
