import Enum

algorithms = [ 
  {
    name: 'Library sort',
    func: library_sort,
    additional_param: [
      0.1, 0.5, 1 # epsilon
    ] 
  },
  {
    name: 'Shell sort',
    func: shell_sort,
    additional_param: [
      [5, 2, 1],
      [10, 5, 2, 1],
      [20, 10, 5, 2, 1]
    ]
  },
  {
    name: 'Quick sort',
    func: quick_sort
  }
]

sequence_lengths = [100000, 500000, 1000000, 200000]

class SequenceTypes(Enum):
  RANDOM = 'RANDOM',
  HALF_SORTED = 'HALF_SORTED',
  SORTED = 'SORTED',
  SORTED_DESCENDING = 'SORTED_DESCENDING'


  