n = int(input())
s = list(map(int, input().split()))
c = 0
r = 0
for i in s:
	if i == -1 and r >= 1:
		r -= 1
	elif i == -1:
		c += 1
	else:
		r += i
print(c)
