#!/usr/bin/python

'''
    https://www.hackerrank.com/challenges/py-set-discard-remove-pop
'''


def performOperation(operation, s, element=None):
    if operation == "pop":
        s.pop()
    elif operation == "remove":
        s.remove(element)
    elif operation == "discard":
        s.discard(element)
    else:
        raise Exception("Unknown operation: %s", operation)
    return s


def main():
    n = input()
    s = set(list(map(int, raw_input().strip().split(" "))))
    x = input()
    for i in range(0, x):
        command = raw_input().strip().split()
        if len(command) > 1:
            s = performOperation(command[0], s, int(command[1]))
        else:
            s = performOperation(command[0], s)
    print sum(s)


if __name__ == '__main__':
    main()
