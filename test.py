__author__ = 'RTryson'

import eulerutils

# N = 10**2
# N = 10**3
N = 10**6

primes = eulerutils.prime_list(N)
print(len(primes)/100)