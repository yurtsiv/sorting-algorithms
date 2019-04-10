import time

def run_algorithm(algorithm, sequence):
  additional_param = algorithm.get('additional_param')
  algorithm_func = algorithm.get('func')

  if (additional_param):
    res = []
    for param in additional_param:
      seq_copy = sequence[:]

      start = time.time()
      algorithm_func(seq_copy, param)
      end = time.time()

      res.append({
        'additional_param': param,
        'exec_time': end - start
      })
    
    return res

  seq_copy = sequence[:]

  start = time.time()
  algorithm_func(seq_copy)
  end = time.time()

  return { 'exec_time': end - start }