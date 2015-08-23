#!/usr/bin/python

'''
	https://www.hackerrank.com/challenges/python-tuples/submissions/code/13268662
'''

from __builtin__ import hash

n = input()
t = raw_input()
t = t.split(" ")
tup = ()
for num in t:
    tInt = int(num)
    tup = tup + (tInt,)  # comma so it is treated as a tuple not an int
print hash(tup)