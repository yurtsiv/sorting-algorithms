from enum import Enum

from library_sort import *
from shell_sort import *
from quick_sort_iterative import *

algorithms = [ 
  {
    'name': 'Library sort',
    'func': library_sort,
    'additional_param': [
      0.5 # epsilon
    ] 
  },
  {
    'name': 'Shell sort',
    'func': shell_sort,
    'additional_param': [
      [10000, 1000, 500, 100, 50, 30, 10, 5, 2, 1],
      [1000, 500, 100, 50, 30, 10, 5, 2, 1],
      [20, 10, 5, 2, 1],
      [10, 5, 2, 1]
    ]
  },
  {
    'name': 'Quick sort',
    'func': quick_sort_iterative,
    'additional_param': None
  }
]

sequence_lengths = [10]

class SequenceTypes(Enum):
  RANDOM = 'RANDOM',
  HALF_SORTED = 'HALF_SORTED',
  SORTED = 'SORTED',
  SORTED_DESCENDING = 'SORTED_DESCENDING'


  