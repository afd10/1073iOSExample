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

def is_rightTrunct(n, primeset):
    listn  = map(int, str(n))
    lenN = len(listn)
    rt = True
    for i in range(0,lenN):
        check =int("".join(map(str, listn[i:])))  
        if check not in primeset:
            rt = False
        
    return rt

def is_leftTrunct(n, primeset):
    listn  = map(int, str(n))
    lenN = len(listn)
    rt = True
    for i in range(lenN,0, -1):
        check =int("".join(map(str, listn[:i])))  
        if check not in primeset:
             
            rt = False
        
    return rt



primelist = primes(1000000)
primeset = set(primelist)


truncPrimes = []

print is_rightTrunct(3797, primeset)
print is_leftTrunct(3797, primeset)

for i in range (4, len(primelist)):
    p = primelist[i]
    if is_rightTrunct(p, primeset) and is_leftTrunct(p, primeset):
        truncPrimes.append(p)

print len(truncPrimes)
print truncPrimes;
print sum(truncPrimes)
        
