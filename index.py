import sys

sys.path.append("./algorithms")
sys.path.append("./simulation")
sys.path.append("./utils")

from simulation import run_simulation 
from library_sort import library_sort

# arr = [10, 7, 4, 2, 7, 4, 3, 1, 10, 9]
# library_sort(arr, 0.5)
run_simulation()