def three_or_five(n):
    if (n%3 == 0 ) or (n%5 == 0):
        return n
    return 0

def sumOf3or5(n):
    total = 0
    for i in range (0,n):
        total = total + three_or_five(i)
    return total

print sumOf3or5(10)
print sumOf3or5(1000)

        
