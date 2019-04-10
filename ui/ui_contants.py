from ui.ui_helpers import *
from algorithms import *

algorithms = [
  {
    'title': 'Bubble sort',
    'func': bubble_sort,  
  },
  {
    'title': 'Bucket sort',
    'func': bucket_sort,
    'get_additional_param': get_bucket_size 
  },
  {
    'title': 'Comb sort',
    'func': comb_sort,
    'get_additional_param': get_shrink_factor
  },
  {
    'title': 'Insertion sort',
    'func': insertion_sort
  },
  {
    'title': 'Shell sort',
    'func': shell_sort,
    'get_additional_param': get_gaps_sequence
  },
  {
    'title': 'Merge sort',
    'func': merge_sort,
  },
  {
    'title': 'Quick sort',
    'func': quick_sort
  }
]