#!/usr/bin/python

'''
	https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
'''

n = input()
l1 = raw_input().split(" ")
list_1 = list(map(int, l1)) 
set_1 = set(list_1)
list_2 = list(set_1)
list_2.sort(reverse=True)
if len(list_2) > 1:
    print list_2[1]
else:
    print list_2[0]