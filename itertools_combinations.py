#!/usr/bin/python

'''
    https://www.hackerrank.com/challenges/itertools-combinations
'''
from itertools import combinations


def main():
    s, k = raw_input().strip().split(' ')
    s = ''.join(sorted(s))
    k = int(k)

    for i in range(1, k+1):
        for y in sorted(list(combinations(s, i))):
            print ''.join(map(str,sorted(y)))

if __name__ == '__main__':
    main()
