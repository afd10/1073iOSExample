
def calcEven(n):
    return n/2

def calcOdd(n):
    return 3*n + 1

def choose(n):
    result = 0
    if n%2 == 0:
        result = calcEven(n)
    else:
        result = calcOdd(n)
    return result

def p14(n):
    count = 1
    while n!=1:
        count+=1
        n = choose(n)
    return count

print "13->", p14(13)

largest = 1
val = 1
for i in range(1,1000000):
    current = p14(i)
    if current > largest:
        print i," : ",current
        largest = current
        val = i
print val

