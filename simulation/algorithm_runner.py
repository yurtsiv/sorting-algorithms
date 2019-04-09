import time

def run_algorithm(algorithm, sequence):
  sequence_copy = sequence[:]
  start = time.time()
  additional_param = algorithm.get('additional_param')
  algorithm_func = algorithm.get('func')
  res = []
  if (additional_param):
    res = algorithm_func(sequence_copy, additional_param[0])
  else:
    res = algorithm_func(sequence_copy)
  
  end = time.time()

  print(sequence)
  print(res)
  return {
    'algorithm': algorithm.get('name'),
    'sequence': len(sequence),
    'execution_time': end - start
  }