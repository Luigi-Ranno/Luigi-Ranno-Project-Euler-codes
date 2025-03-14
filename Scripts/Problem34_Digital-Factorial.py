from math import factorial

factorial_digits = [factorial(i) for i in range(0, 10)]
print(factorial_digits,len(factorial_digits))
def num_same_as_fact_digits(n):
    digits = [int(s) for s in str(n)]

    tot = 0
    for d in digits:
        tot += factorial_digits[d]
        if tot > n:
            return False
    if tot == n:
        return True
    else:
        return False

def check_up_to_n(n):
    tot = 0
    for i in range(3,n+1): # ignore 1 and 2 since 1! and 2! are not sums (as the problem asks)
        if num_same_as_fact_digits(i):
            tot += i
            print(f'Number {i} works')
    return tot

print(check_up_to_n( int(1E6) ))

