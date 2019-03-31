from library_sort import library_sort
from shell_sort import shell_sort
from quick_sort import quick_sort

from simulation_constants import *
from sequence_generator import *
from algorithm_runner import *
from results_handler import *

def run_simulation():
  all_results = []
  for algorithm in algorithms:
    for sequence_length in sequence_lengths:
      for sequence_type in SequenceTypes:
        for sequence_id in range(0, 100):
          seq = generate_sequence(sequence_length, sequence_type, sequence_id)
          result = run_algorithm(algorithm, seq)
          all_results.append(result)

  print_results(all_results)

