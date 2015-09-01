#!/usr/bin/python

'''
    https://www.hackerrank.com/challenges/no-idea
'''


def main():
    happiness = 0
    n, m = raw_input().split(" ")
    candidates = raw_input().strip().split(" ")
    aLike = set(raw_input().strip().split(" "))
    bDislike = set(raw_input().split(" "))

    for item in candidates:
        if item in aLike:
            happiness += 1
        elif item in bDislike:
            happiness -= 1

    print happiness

if __name__ == '__main__':
    main()
