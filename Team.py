n = int(input())
p = 0
for i in range(n):
	s = input()
	v = s.count("1")
	if v >= 2:
		p +=1
print(p)
