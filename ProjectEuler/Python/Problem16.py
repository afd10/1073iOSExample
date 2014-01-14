
sumString =  str(2**1000)

sum = 0
for i in range(0, len(sumString)):
	sum = int(sumString[i]) + sum

print sum
