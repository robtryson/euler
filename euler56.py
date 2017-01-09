__author__ = 'RTryson'

import math

def digitsum(value):
	l = [int(i) for i in str(value)]
	return sum(l)

maxab = 100
max = 0

a = 1
b = 1

while a < maxab:
	while b < maxab:
		v = a**b
		ds = digitsum(v)
		if ds > max:
			max = ds
			print(max,a,b)
		b = b + 1
	b = 1
	a = a + 1