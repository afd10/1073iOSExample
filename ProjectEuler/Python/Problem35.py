from math import sqrt,ceil, factorial


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
#primelist = primes(100)

primeset = set(primelist)

circular = []
keyDict= {}
for i in primelist:
    listn  = map(int, str(i))
    if len(set(listn)) == 1:
        circular.append(i)
    keydigit = "".join(map(str, sorted(listn)))
    if keydigit in keyDict:
        keyDict[keydigit].append(i)
    else:
        keyDict[keydigit] = [i]
#print keyDict


print ">",len(circular)

circPrimes = len(circular)
for key in keyDict:
    keylen = len(key)
    keyset = len(set( map(int, str(key))))
    #print key, ": ", keylen, " : ", keyset, "->", set( map(int, str(key)))
    digcount = factorial(keylen)/factorial(keylen-keyset+2)
    print key, "=>", digcount, " : ",  len(keyDict[key])
    if len(keyDict[key])== digcount and digcount>1:
        print digcount, " : ", key, ":", keyDict[key]
        circPrimes = circPrimes + digcount
        for x in keyDict[key]:
            circular.append(x)

print len(circular)
print circPrimes
print circular
        

