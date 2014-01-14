from math import sqrt

def primes(limit):
    is_prime = range(2,limit) 
    printpr = is_prime[:]
    final_list = []
    

    # set the page
    for i in range(0,len(is_prime)):
        is_prime[i] = True
    print "List Primed ",len(is_prime) 


#    for i in range (0, len(is_prime)):
        #print is_prime
#        if is_prime[i]:
#            for j in range (i+1, len(is_prime)):
                #print "%d>>%d: " %(printpr[i],j)
#                if printpr[j] % printpr[i] == 0:
#                    is_prime[j] = False
                    #print "%d : false" % printpr[j]
#        else:
#            print printpr[i], " is false"


    for i in range(0, len(is_prime)):
        if is_prime[i]:
            
            for j in range (i+printpr[i], len(is_prime), printpr[i]):
                is_prime[j]=False
    print is_prime
    

    for i in range(0,len(is_prime)):
        if is_prime[i]:
            final_list.append(printpr[i])

    return final_list


primeslist = primes(2000000)
#primeslist = primes(10)
total = 0
for i in range (0, len(primeslist)):
    total += primeslist[i]

print "total: ", total
