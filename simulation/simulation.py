from simulation_constants import *
from sequence_generator import *
from algorithm_runner import *
from results_handler import *

def run_simulation():
  all_results = {} 

  for algorithm in algorithms:
    alg_name = algorithm.get('name')
    all_results[alg_name] = {}

    print(algorithm.get('name'))
    for sequence_length in sequence_lengths:
      all_results[alg_name][sequence_length] = {}

      print("Seq. len: " + str(sequence_length))
      for sequence_type in SequenceTypes:
        seq_type_str = str(sequence_type)
        print("Seq. type: " + seq_type_str)

        all_results[alg_name][sequence_length][seq_type_str] = { 'all_results': [] } 

        for id in range(0, 100):
          print("Seq. id: " + str(id))
          
          seq = generate_sequence(sequence_length, sequence_type)
          result = run_algorithm(algorithm, seq)
          all_results[alg_name][sequence_length][seq_type_str]['all_results'].append(result)
  
  handle_result(all_results)
  print("Simulation is finished.")
