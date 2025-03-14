def find_partition_divisible_by(limit):
    """
    Find the first integer whose partition count is divisible by the given limit.
    Uses Euler's Pentagonal Number Theorem for efficiency.
    """
    partitions = [1]  # Base case: p(0) = 1
    n = 1

    while True:
        partition_value = 0
        k = 1

        while True:
            pentagonal1 = k * (3 * k - 1) // 2  # Generalized pentagonal number
            pentagonal2 = k * (3 * k + 1) // 2

            if pentagonal1 > n and pentagonal2 > n:
                break

            sign = -1 if (k % 2 == 0) else 1  # Alternating sign in the formula

            if pentagonal1 <= n:
                partition_value += sign * partitions[n - pentagonal1]
            if pentagonal2 <= n:
                partition_value += sign * partitions[n - pentagonal2]

            k += 1

        partition_value %= limit  # Only store remainder to optimize memory
        partitions.append(partition_value)

        if partition_value == 0:
            return n

        n += 1


# Example usage
result = find_partition_divisible_by(int(1E6))
print(f"First integer whose partition count is divisible by 1E6: {result}")





