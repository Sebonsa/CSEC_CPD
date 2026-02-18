s = input()
t = input()
m = 0
for i in range(len(t)):
	if s[m] == t[i]:
		m += 1
print(m+1)
