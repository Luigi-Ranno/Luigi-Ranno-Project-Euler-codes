def compute_last_10_digits():
    dig = int(10**10)
    part1 = pow(2,7830457,dig)
    part2 = (part1*28433 +1)%dig
    return part2


print(compute_last_10_digits())