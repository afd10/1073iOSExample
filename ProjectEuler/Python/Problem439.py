7
from math import sqrt,ceil

factorDict = {}
ddict = {}

def find_factors(n):
    if n in factorDict:
        return factorDict[n]
    else :
        factors = set([n])
        for i in range(1,int(ceil(sqrt(n)))+1):
            if n%i==0:
                factors.add(i)
                factors.add(n/i)
        #factorDict[n] = factors
        print factors
        return factors

def d(k):
    if k in ddict:
        return ddict[k]
    else:
        factors = find_factors(k)
        ddict[k]=sum(factors)
        #print k, " : ", factors, ":", sum(factors)
        return sum(factors)

def S(n):
    subsum = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            dret = d(i*j)
            subsum = subsum + dret
    print "Sum: ", subsum


#
"""You are given that S(103) = 
563576517282 
252411811549

and S(105) mod 109 = 215766508.
Find S(1011) mod 109."""

for i in range (1,100):
    S(i)

S(10**2)
S(10**3)
#S(10**4)
#print S(10**5) % 10**9
