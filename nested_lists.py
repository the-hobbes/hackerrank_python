#!/usr/bin/python

'''
  https://www.hackerrank.com/challenges/nested-list
'''

def findSecondLowest(l):
    lowest = l[0][1]
    for item in l:
        if item[1] > lowest:
            return item[1]

def main():
    n = input()
    l = []
    for i in range(0, n):
        student = raw_input()
        score = input()
        l.append([student, score])

    l.sort(key=lambda x: x[1])  # use lambda to sort nested list by 2nd element
    secondLowest = findSecondLowest(l)
    names = []
    for item in l:
        if item[1] == secondLowest:
            names.append(item[0])
    names.sort()
    for name in names:
        print name


if __name__ == '__main__':
    main()
