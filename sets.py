#!/usr/bin/python

'''
	https://www.hackerrank.com/challenges/sets

	The symmetric difference of two sets is the collection of elements which are members of either set but not both
	 - in other words, the union of the sets excluding their intersection
'''

def main():
	n = input()
	l1 = raw_input().split(" ")
	list_1 = list(map(int, l1))  # instead of a loop, map the type
	set_1 = set(list_1)

	m = input()
	l2 = raw_input().split(" ")
	list_2 = list(map(int, l2))
	set_2 = set(list_2)

	# union(), intersection() and difference() are common set ops
	u = set_1.union(set_2)
	sect = set_1.intersection(set_2)
	
	for item in sorted(u.difference(sect)):
		print item


if __name__ == '__main__':
	main()