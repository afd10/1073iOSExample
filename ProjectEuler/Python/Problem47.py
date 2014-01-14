from math import sqrt,ceil


def primes(limit):
    is_prime = range(2,limit) 
    printpr = is_prime[:]
    final_list = []
    

    # set the page
    for i in range(0,len(is_prime)):
        is_prime[i] = True
    print "List Primed ",len(is_prime) 


    for i in range(0, len(is_prime)):
        if is_prime[i]:
           final_list.append(printpr[i]) 
           for j in range (i+printpr[i], len(is_prime), printpr[i]):
                is_prime[j]=False

    return final_list


def factors(n, primes):
    factorset = set([])
    for i in primes:
        if n%i == 0:
            factorset.add(i)


primelist = primes(1000000)
primeset = set(primelist)

print primelist[0]

consecutive4 = []
current = 10
while len(consecutive4) < 4:
    current = current + 1
    print current
    factors = set([])
    i = 0
    while primelist[i] <  current:
        if current % primelist[i] == 0:
            factors.add(primelist[i])
        i = i+1
    print factors
    if len(factors) <4:
        consecutive4= []
    else:
        print current
        consecutive4.append(current)
print consecutive4

