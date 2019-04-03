from simulation_constants import *
from sequence_generator import *
from algorithm_runner import *
from results_handler import *

def run_simulation():
  all_results = []
  for algorithm in algorithms:
    print(algorithm.get('name'))
    for sequence_length in sequence_lengths:
      print("Seq. len: " + str(sequence_length))
      for sequence_type in SequenceTypes:
        print(sequence_type)
        for sequence_id in range(0, 100):
          seq = generate_sequence(sequence_length, sequence_type)
          result = run_algorithm(algorithm, seq)
          print(result)
          all_results.append(result)

  print(all_results)
