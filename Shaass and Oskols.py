n = int(input())
bw = list(map(int, input().split()))
l = len(bw)
m = int(input())
for i in range(m):
	w, b = map(int, input().split())
	if w - 2 >= 0:
		bw[w - 2] += b - 1		
	if l > w:
		bw[w] += bw[w-1] - b
	bw[w-1] = 0
for i in bw:
	print(i)
