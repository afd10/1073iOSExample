from math import sqrt, ceil


def factorsOfN(n):
    factors  = []
    sqrtn = sqrt(n)
    for x in range (1, int(ceil(sqrtn))):
        if (n % x == 0):
            factors.append(x)
    return factors

def isPrime(factors):
    return len(factors) == 1

def primeFactors(n):
    pf = []
    factorList = factorsOfN(n)
    for i in factorList:
        if isPrime(factorsOfN(i)):
            pf.append(i)
    return pf

print factorsOfN(13195)
print primeFactors(13195)
print primeFactors(600851475143)[-1]

