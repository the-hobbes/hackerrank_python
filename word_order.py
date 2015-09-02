#!/usr/bin/python
'''
    https://www.hackerrank.com/challenges/word-order
'''


import collections

n = input()
raw_words = []

for i in range(0, n):
    x = raw_input().strip()    
    raw_words.append(x)

words = collections.OrderedDict.fromkeys(raw_words)  # use ordered dict instead of set so that order is preserved

print len(words)  # number of distinct words

for word in words.keys():  # count of each word in original output
    print raw_words.count(word),  # the ',' causes print output on the same line
