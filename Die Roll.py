y, w = map(int, input().split())
p = 6 - max(y, w) + 1
if p == 1:
	print("1/6")
elif p == 2:
	print("1/3")
elif p == 3:
	print("1/2")
elif p == 4:
	print("2/3")
elif p == 6:
	print("1/1")
else:
	print("5/6")
