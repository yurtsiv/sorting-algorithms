import json

def handle_result(results):
  for alg in results:
    alg_exec_times = []
    
    for seq_len in results[alg]:
      seq_len_times = []

      for seq_type in results[alg][seq_len]:
        seq_type_times = []

        for exec_res in results[alg][seq_len][seq_type]['all_results']:
          if isinstance(exec_res, list):
            for add_params_res in exec_res:
              exec_time = add_params_res['exec_time']
              alg_exec_times.append(exec_time)
              seq_len_times.append(exec_time)
              seq_type_times.append(exec_time)
          else:
            exec_time = exec_res['exec_time']
            alg_exec_times.append(exec_time)
            seq_len_times.append(exec_time)
            seq_type_times.append(exec_time)

        results[alg][seq_len][seq_type]['exec_times'] = seq_type_times       
      results[alg][seq_len]['exec_times'] = seq_len_times
    results[alg]['exec_times'] = alg_exec_times



  print("Writing result to simulation_results.json")

  with open('simulation_results.json', 'w') as outfile:  
    json.dump(results, outfile, indent=2)