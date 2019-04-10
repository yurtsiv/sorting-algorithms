import time

from ui.ui_helpers import get_int, get_seq_len, get_seq_type 
from ui.ui_contants import algorithms
from simulation import generate_sequence

def print_main_menu():
  print("\n")
  for i in range(0, len(algorithms)):
    print(str(i) + ") " + algorithms[i]['title'])

def run_ui():
  run = True
  while run: 
    print_main_menu()  
    selected_item = get_int("\nChoose an algorithm", 0, len(algorithms) - 1)
    algorithm = algorithms[selected_item]
    seq = generate_sequence(get_seq_len(), get_seq_type()) 
    print("\nGenerated sequence: ")
    print(seq)

    sorted_seq = None
    if 'get_additional_param' in algorithm:
      add_param = algorithm['get_additional_param'](seq)
      start = time.time()
      sorted_seq = algorithm['func'](seq, add_param)
      end = time.time()
      print("\nExecution time: " + str(end - start))
    else:
      start = time.time()
      sorted_seq = algorithm['func'](seq)
      end = time.time()
      print("\nExecution time: " + str(end - start))
    
    print("\nSorted sequence:")
    print(sorted_seq)