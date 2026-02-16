f = list(input().split())
s = list(input().split())
t = list(input().split())
fr = list(input().split())
ff = list(input().split())

rs = [f, s, t, fr, ff]
for r in rs:
	if r.count("1") == 1:
		nr = rs.index(r) + 1
		nc = r.index("1") +1
		break
m = abs(nr - 3) + abs(nc - 3)
print(m)
