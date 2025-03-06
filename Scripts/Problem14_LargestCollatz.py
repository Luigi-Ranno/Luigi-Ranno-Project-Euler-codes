import numpy
import numpy as np


def Next_Collatz(n):
    if n%2==0:
        return int(n/2)
    else: return int(3*n +1)

def Find_Collatz_seq(start):
    sequence = [start]
    while sequence[-1] != 1:
        next_entry = Next_Collatz(sequence[-1])
        sequence.append(next_entry)
    return sequence



numbers_to_test = np.arange(1,1000000.1,1)
associated_seq_len = []
associated_seq = []
for number_to_test in numbers_to_test:
    seq = Find_Collatz_seq(number_to_test)
    seq_len = len(seq)
    associated_seq_len.append(seq_len)
    associated_seq.append(seq)

max_len = np.max(associated_seq_len)
max_idx = np.argmax(associated_seq_len)
max_start = numbers_to_test[max_idx]
print(f'The maximum number is {max_start}\n'
      f'It corresponds to a sequence of length:{max_len}')

