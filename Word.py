s = input()
l = 0
c = 0
for i in s:
	if i.islower():
		l += 1
	else:
		c += 1
if c > l:
	print(s.upper())
else:	
	print(s.lower())
