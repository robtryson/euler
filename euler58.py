# euler58.py

# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49

# It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

# If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

import eulerutils
import sys

def find_answer(maxside):
	if maxside == 1:
		return False
	pl = eulerutils.prime_list(maxside**2)

	odds = [n for n in range(1,maxside**2+1,2)]
	diags = list()
	i = 0
	layer = 0
	layerend = 0
	while i < len(odds):
		diags.append(odds[i])
		if i >= layerend:
			layer += 1
			layerend += 4*layer
		i += layer
	
	primediags = list()
	for d in diags:
		if d in pl:
			primediags.append(d)
	ratio = len(primediags) / len(diags)
	print("Side length: ", maxside)
	print("Ratio: ", ratio)
	return ratio < 0.1
	
# to add a new layer - really only care about the numbers on the diags
# just need oldmax and layer

# number of diagonals = 4*layer + 1
# on a layer, max value is (2*layer+1)**2
# step value is equal to layer

layer = 0
ratio = 1
side = 1
print("calculating prime list")
pl = eulerutils.prime_list_arr(10**9)
print("done")
pcount = 0

layer = 8659
pcount = 3638

while ratio > 0.1:
	layer += 1
	step = 2*layer
	max = (2*layer+1)**2
	min = (2*(layer-1)+1)**2
	side = 2*layer+1
	diags = list(range(min+step, max+1, step))
	for x in diags:
		if pl[x]:
			pcount += 1
	print(diags)
	numdiags = 4*layer + 1
	ratio = pcount / numdiags
	print(side, ratio)

sys.exit()	
	
side = 3001 #0.1333
flag = False
while not flag:
	flag = find_answer(side)
	side += 2