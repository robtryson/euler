# euler60.py
__author__ = "RTryson"

# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

import eulerutils

# generate pairs that fit the criteria
# e.g. 3 and 7 makes 37 and 73 so note [3,7]

maxval = 10**4
maxprime = 10**6
pl = eulerutils.prime_list_arr(maxprime)

# this is not great so far and probably won't scale well
# try to think of a better algorithm

pairs = list()
for check,v in enumerate(pl[:maxval]):
	if v and check > 2: # 2 will never be in a family
		print(check)
		for kk,vv in enumerate(pl[check:]):
			if vv and kk > check:
				l = int(str(kk)+str(check))
				r = int(str(check)+str(kk))
				if l < maxprime and r < maxprime and pl[l] and pl[r]:
					pairs.append([check,kk])
print(pairs)