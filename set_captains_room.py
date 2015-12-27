#!/usr/bin/python

'''
    https://www.hackerrank.com/challenges/py-the-captains-room
'''


def main():
    n = input() 
    rooms = raw_input().strip().split(" ")
    rooms.sort()

    for i in range(0, len(rooms), n):
      if (rooms[i] != rooms[(i+1)%len(rooms)]): # use mod to compare the tail to the head
        print rooms[i]
        break

if __name__ == '__main__':
    main()

