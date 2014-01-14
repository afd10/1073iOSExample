from math import sqrt, ceil

primeList = []

def factors(n):
    factors = []
    for i in range(1,int((ceil(sqrt(n))))+1):
        if (n%i == 0):
            factors.append(i)
    print n, factors
    return factors

def is_Prime(n):
    if len(factors(n)) == 1:
        global primeList
        primeList.append(n)
    #return True


start = 2
while len(primeList) < 10000:
#while len(primeList) < 13:
    print start
    is_Prime(start)
    start += 1

print primeList

