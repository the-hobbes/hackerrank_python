#!/usr/bin/python

'''
    Simple Array Sum
    https://www.hackerrank.com/challenges/simple-array-sum
'''


def main():
    l = input()
    s = raw_input()

    array = s.split(' ')
    total = 0
    for number in array:
        total += int(number)

    print total

if __name__ == '__main__':
    main()
