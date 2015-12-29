'''
    https://www.hackerrank.com/challenges/py-check-strict-superset
    A strict superset has atleast one element which not in its subset.
'''

def main():
  elements_of_a = set(raw_input().strip().split())
  n = input()
  is_superset = True

  for i in range(n):
    elements_of_b = set(raw_input().strip().split())
    if len(elements_of_b) >= len(elements_of_a):
      # if there are more elements in b, then a is defs not a superset of b.
      is_superset = False
    if not elements_of_b.issubset(elements_of_a):
      # if b isn't a subset of a, a defs isn't a superset of b
      is_superset = False

  print is_superset


if __name__ == '__main__':
  main()
