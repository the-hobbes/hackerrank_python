#!/usr/bin/python

'''
    Finding the percentage
    https://www.hackerrank.com/challenges/finding-the-percentage
'''

from __future__ import division  # for python 3 style division

def main():
	students = {}
	n = input() # first line gives how many lines of input
	for i in range(0,n): # each line of input
	    s = raw_input()
	    a = s.split(" ")
	    int_list = [float(n) for n in a[1:]]
	    average = sum(int_list) / len(int_list)
	    students[a[0]] = average
	target = raw_input() # last line gives the target student
	print "{0:.2f}".format(students[target])

if __name__ == '__main__':
	main()

