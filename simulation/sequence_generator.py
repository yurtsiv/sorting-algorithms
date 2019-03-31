import random

from simulation_constants import SequenceTypes 

def get_random_seq(length):
  return [random.randint(0, length) for _ in range(0, length)]

def get_sorted_seq(length):
  return [e for e in range(0, length)]

def get_half_sorted_seq(length):
  return get_sorted_seq(length // 2) + get_random_seq(length // 2)

def get_descending_sorted_seq(length):
  return [e for e in range(length, 0, -1)]

sequence_types_funcs = {
  SequenceTypes.RANDOM: get_random_seq,
  SequenceTypes.HALF_SORTED: get_half_sorted_seq,
  SequenceTypes.SORTED: get_sorted_seq,
  SequenceTypes.SORTED_DESCENDING: get_descending_sorted_seq,
}

def generate_sequence(length, type):
  return sequence_types_funcs[type](length)
