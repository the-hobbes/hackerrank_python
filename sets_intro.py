#!/usr/bin/python

'''
    https://www.hackerrank.com/challenges/py-introduction-to-sets
'''

def main():
    n = input()
    raw_heights = raw_input().strip().split(" ")
    heights = [float(x) for x in raw_heights]
    s = set(heights)
    average = sum(s) / len(s)
    print average



if __name__ == '__main__':
    main()
