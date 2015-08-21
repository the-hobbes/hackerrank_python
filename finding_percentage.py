#!/usr/bin/python

'''
    Finding the percentage
    https://www.hackerrank.com/challenges/finding-the-percentage
'''

from __future__ import division  # for python 3 style division

students = {}
n = input()
for i in range(0,n):
    s = raw_input()
    a = s.split(" ")
    int_list = [float(n) for n in a[1:]]
    average = sum(int_list) / len(int_list)
    students[a[0]] = average
target = raw_input()
print "{0:.2f}".format(students[target])
