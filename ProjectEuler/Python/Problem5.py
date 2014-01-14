

def is_divisable(top_divisor, n):
	for x in range(1, top_divisor):
		if n%x != 0:
			return False
	return True

top = int(raw_input("Top? :"))
n = 5
while not is_divisable(top, n):
	n= n+5

print n
