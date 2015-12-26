#!/usr/bin/python

'''
    https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation
    Symmetric_difference() operator returns a set with all elements that are in 
    set and iterable but not both.
'''


def main():
    n = input()
    english_roll_numbers = set(raw_input().split(" "))
    b = input()
    french_roll_numbers = set(raw_input().split(" "))
    
    # total students subscribed to at least one newspaper
    print len(english_roll_numbers.symmetric_difference(french_roll_numbers))


if __name__ == '__main__':
    main()

