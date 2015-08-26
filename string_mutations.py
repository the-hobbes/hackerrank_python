s1 = raw_input()
s2 = raw_input()
l1 = list(s1)
l2 = s2.split(" ")
i = int(l2[0])
letter = l2[1]

l1[i] = letter
print ''.join(l1)
