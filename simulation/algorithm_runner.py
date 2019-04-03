import time

def run_algorithm(algorithm, sequence):
  start = time.time()
  additional_param = algorithm.get('additional_param')
  algorithm_func = algorithm.get('func')
  if (additional_param):
    algorithm_func(sequence, additional_param[0])
  else:
    algorithm_func(sequence)
  
  end = time.time()

  return {
    'algorithm': algorithm.get('name'),
    'sequence': len(sequence),
    'execution_time': end - start
  }