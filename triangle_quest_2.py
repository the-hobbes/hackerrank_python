'''
    https://www.hackerrank.com/challenges/triangle-quest-2
    Make a palindromic triange
'''


def main():
  for i in range(1,int(raw_input())+1): 
    print ((10**i//9)**2)


if __name__ == '__main__':
  main()


