#!/usr/bin/python

'''
  https://www.hackerrank.com/challenges/find-a-string/submissions/code/13392979
'''

import re

searchIn = raw_input()
searchFor = raw_input()

# regex idea from http://stackoverflow.com/questions/5616822/python-regex-find-all-overlapping-matches
matches = re.finditer(r'(?=(' + searchFor + '))',searchIn)
results = [match.group(1) for match in matches]
print len(results)

