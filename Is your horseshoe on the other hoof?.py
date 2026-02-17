s = input().split()
s.sort()
n = len(s)
b = 0
for i in range(1, n):
	if s[i] == s[i-1]:
		b += 1
print(b)
