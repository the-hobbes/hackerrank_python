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
    size_diff = len(elements_of_a) - len(elements_of_b)
    set_diff = len(elements_of_a.difference(elements_of_b))
    # if the difference between the sets is greater than just the difference
    # of the size of the sets, we know that there are additional differences in
    # the elements of the set?
    if set_diff <= size_diff:
      is_superset = False

  print is_superset


if __name__ == '__main__':
  main()
