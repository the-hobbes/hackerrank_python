#!/usr/bin/python

'''
    Finding the percentage
    https://www.hackerrank.com/challenges/python-lists
'''

L = []

def runCommand(command, args):
	int_list = None
	if len(args) > 0 and args[0] != "":
		int_list = [int(arg) for arg in args]

	if command == "insert":
		if int_list:
			L.insert(int_list[0], int_list[1])
	elif command == "print":
		print L
	elif command == "remove":
		for i in int_list:
			L.remove(i)
	elif command == "append":
		for i in int_list:
			L.append(i)
	elif command == "sort":
		L.sort()
	elif command == "pop":
		if int_list:
			for i in int_list:
				L.pop(i)
		else:
			L.pop()
	elif command == "reverse":
		L.reverse()
	else:
		print "Command %s not found" % command

def main():
	n = input()
	for i in range(0,n):
		line = raw_input()
		line = line.split(" ")
		command = line[0]
		args = line[1:]
		runCommand(command, args)

if __name__ == '__main__':
	main()