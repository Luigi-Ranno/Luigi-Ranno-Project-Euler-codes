import numpy as np

def pentagonal_number(p):

    return int(p*(3*p-1 )/2)

def pentagon_index(n):
    return (1 + np.sqrt( float(1+24*n) ))/6

def is_sum_pentagonal(a,b):
    s = a+b
    return pentagon_index(s).is_integer()
def is_difference_pentagonal(a,b):
    d = a-b
    return pentagon_index(d).is_integer()


n1 = 2
n2 = 1

done = False

while not done:
    p1 = pentagonal_number(n1)
    while n2<n1:
        p2 = pentagonal_number(n2)

        if is_sum_pentagonal(p1,p2) and is_difference_pentagonal(p1,p2):
            print(f'Found pentagonal numbers with pentagonal difference and sum\n'
                  f'The numbers are:{p1} ({n1}th number) and {p2} ({n2}th number)')
            done=True


        n2+=1

    n1+=1
    n2=1

