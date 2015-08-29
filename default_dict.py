#!/usr/bin/python

'''
    https://www.hackerrank.com/challenges/defaultdict-tutorial
'''

from collections import defaultdict


def main():
    inputs = raw_input().split(" ")
    n, m = int(inputs[0]), int(inputs[1])
    d = defaultdict(list)

    for i in range(0, n):
            item = raw_input()
            d[item].append(i+1)

    for i in range(0, m):
        key = raw_input()
        print " ".join(str(indecies) for indecies in d[key])


if __name__ == '__main__':
    main()
