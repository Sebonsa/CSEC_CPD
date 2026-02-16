n = int(input())
lm = []
for i in range(n):
	lm.append(input())
g = 1
for i in range(1, n):
	if lm[i][0] == lm[i-1][1]:
		g += 1
print(g)
