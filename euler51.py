__author__ = 'RTryson'

import eulerutils
import sys

# By replacing the 1st digit of the 2-digit number *3, it turns out that 
# six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 
# 5-digit number is the first example having seven primes among the ten 
# generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. 
# Consequently 56003, being the first member of this family, is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number 
# (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

def looksBinary(num):
	l = [int(x) for x in str(num)]
	flag = True
	for n in l:
		if n > 1:
			flag = False
	return flag
	
def checkValid(start, pattern):
	pattern = list(str(pattern))
	numstr = str(start)
	l = len(numstr)
	while len(pattern) < l:
		pattern.insert(0,'0')
	check = -1
	flag = True
	for i, x in enumerate(pattern):
		if x == '1' and flag:
			if check == -1:
				check = numstr[i]
			elif numstr[i] != check:
				flag = False
	return flag
	
def makeFamily(start, pattern):
	pattern = list(str(pattern))
	numstr = str(start)
	l = len(numstr)
	# print(l,pattern)
	while len(pattern) < l:
		pattern.insert(0,'0')
	# print(pattern)
	# print(numstr)
	#print(int(''.join(pattern)))
	result = list()
	# generate num to add to family
	for dig in range(0,10):
		number = list()
		for i, x in enumerate(pattern):
			if x == '0':
				number.append(int(numstr[i]))
			else:
				number.append(dig)
		number = ''.join(str(n) for n in number)
		result.append(int(number))
		
	return result

maxpower = 6
maxbin = 2**maxpower-1
maxprime = 10**maxpower
lowend = maxprime / 10
pl = eulerutils.prime_list(lowend,maxprime)
#pl = pl[4:] #get rid of one-digit primes
#print(pl)

bindiffs = list()
for i in range(1,maxbin):
	# bin(i) returns '0bxxxxx'
	# get rid of the '0b', then convert to int
	b = int(bin(i)[2:])
	if b % 2 == 0:
		bindiffs.append(b)

candidates = list()

# instead of finding diff with ENTIRE LIST (~10**maxpower)
# generate binary-ish differences and see if in list

for index, check in enumerate(pl):
	print(check)
	for bd in bindiffs:
		if checkValid(check,bd) and (check+bd) in pl:
			candidates.append([check,bd])
	# complist = pl[index:]
	# difflist = [x - check for x in complist]
	# print(difflist)
	# for diff in difflist[1:]:
		# if looksBinary(diff):
			# candidates.append([check, diff])

# This does NOT YET WORK
# for example there are lots of primes separated by multiples of 100
# need to do some string manip based off of the binary-ish differences
# for example, 56003 -> 56113, diff of 110
# take the non-0 digits and replace those digits in the checkable nums
# starting from 56003: check 56xx3
# find families, then count	

print(candidates)
winner = list()
winnerlength = 0
eights = list()
for c in candidates:
	start = c[0]
	pattern = c[1]
	result = list([start])
	
	fam = makeFamily(start, pattern)
	result = list()
	for n in fam:
		if n in pl:
			result.append(n)
	
		
	result.sort()
	
	if len(result) == 8:
		eights.append(result)
	
	if len(result) > winnerlength:
		winnerlength = len(result)
		winner = list(result)
	print(result, len(result))
	
print("Eights:")
print(eights)
print("Winner is:")
print(winnerlength, winner)