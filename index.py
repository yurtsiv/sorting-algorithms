import sys

sys.path.append("./algorithms")
sys.path.append("./simulation")

import sequence_generator
from simulation_constants import *

print(sequence_generator.generate_sequence(20, SequenceTypes.SORTED_DESCENDING))