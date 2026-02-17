n = int(input())
h = []
g = []
for i in range(n):
	a, b = input().split()
	h.append(a)
	g.append(b)
c = 0
for i in h:
	c += g.count(i)
print(c)
