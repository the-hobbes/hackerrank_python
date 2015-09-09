#!/usr/bin/python

'''
    https://www.hackerrank.com/challenges/piling-up
'''


from collections import deque


def computeVerticalStack(lengthOfTestCase, testCase):
    exit = False
    while not exit:
        if len(testCase) == 0:
            break
        else:
            maximum = max(testCase)
            left = testCase[0]
            right = testCase[-1]
            if left == maximum:
                testCase.popleft()
            elif right == maximum:
                testCase.pop()
            else:
                exit = True
                return "No"
    if not exit:
        return "Yes"


def main():
    numberOfTestCases = input()
    for i in range(0, numberOfTestCases):
        lengthOfTestCase = input()
        testCase = raw_input().split(" ")
        intCase = deque([int(x) for x in testCase])
        print computeVerticalStack(lengthOfTestCase, intCase)

if __name__ == '__main__':
    main()
