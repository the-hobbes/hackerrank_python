#!/usr/bin/python

'''
    https://www.hackerrank.com/challenges/itertools-combinations
'''
from itertools import combinations


def main():
    s, k = raw_input().strip().split(' ')
    k = int(k)

    for i in range(1, k+1):
        print sorted(list(combinations(s, i)))

if __name__ == '__main__':
    main()
