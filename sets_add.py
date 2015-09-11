#!/usr/bin/python

'''
    https://www.hackerrank.com/challenges/py-introduction-to-sets
'''

def main():
    n = input()
    stamps = set()
    for i in range(0, n):
        stamps.add(raw_input().strip())
    print len(stamps)


if __name__ == '__main__':
    main()
