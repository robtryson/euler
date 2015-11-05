__author__ = 'rtryson'

import math

# How many Lychrel numbers are there below 10,000?
# Definition of Lychrel numbers:
#   reverse the number and add the reverse to the original
#   if this is a palindrome, done
#   else repeat (max 50 iterations)

def rev(num):
    s = str(num)
    r = s[::-1]
    return int(r)

def check_pal(num):
    check = True
    s = str(num)
    l = len(s)
    front = s[:l//2]
    back = s[math.ceil(l/2):]
    back = back[::-1]
    return front == back

def iterate(num):
    num += rev(num)
    return num

max_iter = 50
max_num = 10000
count = 0

for i in range(1,max_num+1):
    it = 0
    n = iterate(i)
    it += 1
    while not check_pal(n) and it < max_iter:
        n = iterate(n)
        it += 1
    if check_pal(n):
        print(i, n)
        count += 1

print(count)