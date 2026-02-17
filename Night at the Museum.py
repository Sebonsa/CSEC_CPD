import string

em = string.ascii_lowercase
n = input()
m = 0
p = "a"
for c in n:
	if em.index(p) < em.index(c):
		m += min(em.index(c) - em.index(p), em.index(p) + (len(em) - em.index(c)))
	elif em.index(c) < em.index(p):
		m += min(em.index(p) - em.index(c), (len(em) - em.index(p) + em.index(c)))
	p = c
print(m)
