#!/usr/bin/python

'''
    https://www.hackerrank.com/challenges/py-set-intersection-operation
'''


def main():
    n = input()
    english_roll_numbers = set(raw_input().split(" "))
    b = input()
    french_roll_numbers = set(raw_input().split(" "))
    
    # total students subscribed to both newspapers
    print len(english_roll_numbers.intersection(french_roll_numbers))


if __name__ == '__main__':
    main()

