
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
            
            for j in range (i+printpr[i], len(is_prime), printpr[i]):
                is_prime[j]=False
    #print is_prime
    

    for i in range(0,len(is_prime)):
        if is_prime[i]:
            final_list.append(printpr[i])

    return final_list


primeslist = primes(10000000)
primeset = set(primeslist)
print "Prime List ", len(primeslist)




digits = []
for i in range (1,10):
    digits.append(i)
    print digits
    for prime in primeslist:
        #print i, " : ", 10**i , " : ", 10**(i)    
        if prime > 10**(i-1) and prime < 10**i:
            iset = set(list(str(prime)))
            #print "iset: ", iset
            if len(iset) > i-1:
                check = 0
                #print "i:", prime, " : ", iset
                for j in digits:
                    #print j, iset
                    if str(j) in iset:
                        print "Got 1: ", j, "/", i
                        check = check + 1
                #print "check:", prime, " : ", check
                if check == i :
                    print "REALPRIME:", prime 
