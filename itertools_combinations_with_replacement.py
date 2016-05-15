#!/usr/bin/python

'''
    https://www.hackerrank.com/challenges/itertools-combinations-with-replacement
'''

from itertools import combinations_with_replacement

def main():
    s, k = raw_input().strip().split(' ')
    s = ''.join(sorted(s))
    k = int(k)

    for y in sorted(list(combinations_with_replacement(s, k))):
        print ''.join(map(str,sorted(y)))


if __name__ == '__main__':
    main()
