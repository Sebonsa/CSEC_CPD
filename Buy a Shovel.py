k, r = map(int, input().split())

if k < 10 and k == r:
	print(1)
elif k<10 and k != r:
	print(0)
else:
	s = k
	while True:
		if s%10 == 0 or s%10 == r:
			break
		else:
			s += k
	print(s//k)
