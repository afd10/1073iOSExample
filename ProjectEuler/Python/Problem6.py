
end = int(raw_input("from 1..? "))
sumOfSquares = 0
sqareOfSum = 0
sum =0

for x in range (1,end+1):
    sumOfSquares += (x*x)
    sum += x

squareOfSum = sum * sum
print "%d - %d = %d" % (squareOfSum, sumOfSquares, squareOfSum - sumOfSquares)
