#!/usr/bin/python

'''
    https://www.hackerrank.com/challenges/py-the-captains-room
'''


def main():
    i = input() # number of elements in set A
    temp = raw_input().strip().split(" ")
    # A = set([int(x) for x in temp])
    
    for item in temp:
      if temp.count(item) == 1:
        print item


if __name__ == '__main__':
    main()

