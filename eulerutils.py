__author__ = 'RTryson'

import math
import numpy as np


def prime_list(maxval):
    # pl initially all 1s
    # set pl[0] = 0, pl[1] = 0
    # starting at pl[2]:
    #   if pl[i] == 1
    #   step = i, check = i+step = 2*i
    #   while check < end (maxval+1):
    #       set pl[check] = 0
    #       check += step
    pl = [1 for maxval in range(0,maxval+1)]
    pl[0] = 0
    pl[1] = 0
    i = 2
    while i <= math.sqrt(maxval):
        if pl[i] == 1:
            step = i
            check = 2*i
            while check <= maxval:
                pl[check] = 0
                check += step
        i += 1
    print(pl)
    b = list()
    for k, v in enumerate(pl):
        if v == 1:
            b.append(k)
    return b
    
def prime_list_ind(maxval):
    pl = [1 for maxval in range(0,maxval+1)]
    pl[0] = 0
    pl[1] = 0
    i = 2
    while i <= math.sqrt(maxval):
        if pl[i] == 1:
            step = i
            check = 2*i
            while check <= maxval:
                pl[check] = 0
                check += step
        i += 1
    return pl
	
def prime_list_arr(maxval):
	pl = np.ones(maxval, dtype=np.bool_)
	pl[0] = 0
	pl[1] = 0
	i = 2
	while i <= math.sqrt(maxval):
        if pl[i] == 1:
            step = i
            check = 2*i
            while check <= maxval:
                pl[check] = 0
                check += step
        i += 1
    return pl
	
def primelist(minval, maxval):
    # pl initially all 1s
    # set pl[0] = 0, pl[1] = 0
    # starting at pl[2]:
    #   if pl[i] == 1
    #   step = i, check = i+step = 2*i
    #   while check < end (maxval+1):
    #       set pl[check] = 0
    #       check += step
    pl = [1 for maxval in range(0,maxval+1)]
    pl[0] = 0
    pl[1] = 0
    i = 2
    while i <= math.sqrt(maxval):
        if pl[i] == 1:
            step = i
            check = 2*i
            while check <= maxval:
                pl[check] = 0
                check += step
        i += 1

    b = list()
    for k, v in enumerate(pl):
        if k > minval and v == 1:
            b.append(k)
    return b

