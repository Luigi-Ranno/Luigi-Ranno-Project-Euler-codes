import numpy as np


def triangle_n(n):
    return int( n*(n+1)*0.5 )

def number_of_divisors(n):
    tot = 0
    for i in range(1,int(np.sqrt(n))+1):
        if n%i == 0:
            tot += 1
            if i != n // i:
                # divisors.append(number // i)
                tot += 1
    return tot

# for i in range(1,8):
#     print(f'{i}th triangle number is: {triangle_n(i)}')

over_target_divs = False
target = 500
curr_n = 1

# print(number_of_divisors(999999))

while not over_target_divs:
    t_n = triangle_n(curr_n)
    num_divs = number_of_divisors(t_n)

    if num_divs > target:
        print(f'Number of divisors for {curr_n}th triangle number\n'
              f'(i.e. {t_n}), is {num_divs}')
        over_target_divs = True
    else: curr_n += 1



