def is_Palindrome(n):
	numString = str(n)
	strlen = len(numString)
	for x in range(0, strlen/2):
		if numString[x] != numString[-(x+1)]:
			return False
	return True 

print "123: ", is_Palindrome(123)
print "910019: ", is_Palindrome(910019)

largest = 0;
for x in range(100,999):
	for y in range (100,999):
		if is_Palindrome(x*y) and (x*y>largest):
			largest = x*y
print largest
