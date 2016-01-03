'''
  https://www.hackerrank.com/challenges/itertools-permutations
'''

from itertools import permutations


def main():
  s, k = raw_input().strip().split()
  k = int(k)
  s = ''.join(sorted(s))
  perms = list(permutations(s, int(k)))

  # now format and print
  for item in perms:
    print ''.join(map(str, item))


if __name__ == '__main__':
  main()
