__author__ = 'RTryson'

import math

# How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?

# just brute-force this one
count = 0
for n in range(1, 101):
    for r in range(0, n):
        num = math.factorial(n)
        den = math.factorial(r) * math.factorial(n - r)
        ncr = num / den
        print(ncr, ncr > 10**6)
        if ncr > 10**6:
            count += 1

print("Answer = ", count)