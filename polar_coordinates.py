'''
    https://www.hackerrank.com/challenges/polar-coordinates
'''

import cmath


def main():
  z = input()  # seems to auto detect complex numbers
  # convert complex number to polar coordinate. polar coordinate consists of
  # phi, the phase angle
  # r, the modulus

  print abs(z)
  print cmath.phase(z) 
  


if __name__ == '__main__':
  main()
