#!/usr/bin/python

'''
    A Very Big Sum
    https://www.hackerrank.com/challenges/a-very-big-sum
'''


def main():
    l = input()
    s = raw_input()

    array = s.split(' ')
    total = long(0)
    for number in array:
        total += long(number)

    print total

if __name__ == '__main__':
    main()
