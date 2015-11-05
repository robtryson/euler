__author__ = 'RTryson'

import math


def prime_list(n):
    # pl initially all 1s
    # set pl[0] = 0, pl[1] = 0
    # starting at pl[2]:
    #   if pl[i] == 1
    #   step = i, check = i+step = 2*i
    #   while check < end (n+1):
    #       set pl[check] = 0
    #       check += step
    pl = [1 for n in range(0,n+1)]
    pl[0] = 0
    pl[1] = 0
    i = 2
    while i <= math.sqrt(n):
        if pl[i] == 1:
            step = i
            check = 2*i
            while check <= n:
                pl[check] = 0
                check += step
        i += 1

    b = list()
    for k, v in enumerate(pl):
        if v == 1:
            b.append(k)
    return b

