#!/usr/bin/python

'''
    https://www.hackerrank.com/challenges/py-set-mutations
'''


def setFunctionMapping(function_name, set_1, set_2):
  '''
    Updates a given set via a passed in function.
    Params:
      function_name, the type of set operation to be performed
      set_1, the set the function is being applied to
      set_2, the set that the original set will be modified by
  '''
      
  if function_name == 'update':
    set_1.update(set_2)
  elif function_name == 'intersection_update':
    set_1.intersection_update(set_2)
  elif function_name == 'difference_update':
    set_1.difference_update(set_2)
  elif function_name == 'symmetric_difference_update':
    set_1.symmetric_difference_update(set_2)

  return set_1


def main():
    i = input() # number of elements in set A
    temp = raw_input().strip().split(" ") # space separated list of elements of set A.
    A = set([int(x) for x in temp])
    n = input() # number of other sets
    for i in range(0,n*2):
      try:
        op = raw_input().strip().split(" ")[0] 
        temp_S = raw_input().strip().split(" ")
        S = set([int(x) for x in temp_S])
        A = setFunctionMapping(op, A, S)
      except(EOFError):
        break # end of file

    print sum(A)

if __name__ == '__main__':
    main()

