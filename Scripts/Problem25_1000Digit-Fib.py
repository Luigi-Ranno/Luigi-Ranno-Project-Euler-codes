import numpy as np

def Next_Fib(prev,prev_prev):
    return prev + prev_prev

wanted_number_digits = 1000
max_number_of_digits = 0

Fibs = [1,1]

while max_number_of_digits < wanted_number_digits:
    prev = Fibs[-1]
    prev_prev = Fibs[-2]
    next_fib = Next_Fib(prev,prev_prev)
    Fibs.append(next_fib)

    len_digits = len(str(next_fib))
    if len_digits > max_number_of_digits:
        max_number_of_digits = len_digits
# print(Fibs)
print(len(Fibs))





