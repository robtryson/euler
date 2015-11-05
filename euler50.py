__author__ = 'RTryson'

import eulerutils

# N = 10**2
# N = 10**3
N = 10**6

primes = eulerutils.prime_list(N)
start = 0
candidates = {}

# kind of a BS/empirically derived endpoint but it turned out to be correct in the end
while start <= len(primes)/100:
    print(start)
    i = start
    next_sum = 0
    check_list = []
    while next_sum < N:
        check_list.append(primes[i])
        current_sum = sum(check_list)
        next_sum = current_sum + primes[i+1]
        i += 1
        # print(current_sum, check_list)
        if current_sum in primes:
            if candidates.get(current_sum) is None or candidates.get(current_sum) < len(check_list):
                candidates[current_sum] = len(check_list)
    start += 1

# start with full list?

# below block prints max of lengths
maxlen = 0
current = []
for i in candidates.items():
    p = i[0]
    l = i[1]
    print(p,l)
    if l > maxlen:
        maxlen = l
        current = i

print(current)