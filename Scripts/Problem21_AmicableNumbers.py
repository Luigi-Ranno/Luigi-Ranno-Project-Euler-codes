import numpy as np

def find_d(n):
    tot = 0
    for i in range(1,n):
        if n%i == 0:
            # print(i)
            tot += i
    return tot

d_ns = {}
am_numbs = []

# for i in range(2,286):
#     d = find_d(i)
#     if d>1:
#         if d in list(d_ns.keys()):
#             print(f'Found amicable pair between {d_ns[d]} and {i}')
#         else: d_ns[d] = i

amicable_pairs = []
for i in range(2,10000+1):

    b = find_d((i))
    a = find_d(b)

    if a != b and a==i:
        # print(f' Found amicable numbers {a} and {b} ')
        min_n = min(a,b)
        max_n = max(a,b)
        pair = [min_n,max_n]
        if pair not in amicable_pairs:
            print(f' Found new amicable numbers {a} and {b} ')

            amicable_pairs.append(pair)

print(amicable_pairs)

tot = 0
for pair in amicable_pairs:
    for numb in pair:
        tot += numb
print(f'Total is: {tot}')

# d_ns[10] = 22
# print( list(d_ns.keys())  )





