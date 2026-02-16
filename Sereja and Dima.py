n = int(input())
c = list(map(int, input().split()))
s = 0
d = 0
for i in range(n):
	p = max(c[0], c[-1])
	if i%2 == 0:
		s += p
	else:
		d += p
	c.remove(p)
print(s, d)
