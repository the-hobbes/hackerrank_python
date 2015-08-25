#!/usr/bin/python

'''
    https://www.hackerrank.com/challenges/list-comprehensions
'''

def nonListComprehension(x, y, z, n):
    l = []
    for i in range(0, x + 1):
        for o in range(0, y + 1):
            for p in range(0, z + 1):
                if i + o + p != n:
                    l.append([i, o, p])
    l.sort()
    print l

def listComprehension(x, y, z, n):
    l = []
    newL = [l.append([i, o, p]) for i in range(0, x + 1) for o in range(0, y + 1) for p in range(0, z + 1) if i + o + p != n]
    l.sort()
    print l

def main():
    x = input()
    y = input()
    z = input()
    n = input()

    # nonListComprehension(x, y, z, n)
    listComprehension(x, y, z, n)

if __name__ == '__main__':
    main()
