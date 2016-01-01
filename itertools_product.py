'''
  https://www.hackerrank.com/challenges/itertools-product
  itertools.product()
  Equivalent to nested for-loops in a generator expression. For example, 
  product(A, B) returns the same as ((x,y) for x in A for y in B).
'''


from itertools import product


def main():
  list_a = raw_input().strip().split()
  list_a = [int(x) for x in list_a]
  list_b = raw_input().strip().split()
  list_b = [int(x) for x in list_b]

  L = [list_a, list_b]
  print ' '.join(map(str, list(product(*L))))
  list(product(*L))

if __name__ == '__main__':
  main()
