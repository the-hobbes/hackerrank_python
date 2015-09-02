#!/usr/bin/python
'''
    https://www.hackerrank.com/challenges/word-order
'''


import collections

n = input()
raw_words = []
words = collections.OrderedDict()

for i in range(0, n):
    x = raw_input().strip()
    if words.get(x):
        words[x] += 1
    else:
        words[x] = 1

print len(words)
for item in words:
    print words.get(item),