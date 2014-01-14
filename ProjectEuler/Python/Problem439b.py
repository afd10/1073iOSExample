
def primes(limit):
    is_prime = range(2,limit) 
    printpr = is_prime[:]
    prime_list = []
    
    # set the page
    for i in range(0,len(is_prime)):
        is_prime[i] = True
    print "List Primed ",len(is_prime) 


    for i in range(0, len(is_prime)):
        if is_prime[i]:
            prime_list.append(printpr[i])
            for j in range (i+printpr[i], len(is_prime), printpr[i]):
                is_prime[j]=False


    return prime_list




def S(n):
    subsum = 0
    limit = n**2 +1
    primes= primes(limit)
    

    print "Setup complete"
    print factors
    for i in range(1, n+1):
        for j in range(1, n+1):
            subsum = subsum + sum(factors[i*j])

    print subsum

print factorizer(1000)
S(3)
#S(10**3)
