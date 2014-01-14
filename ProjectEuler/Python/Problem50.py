
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


primeslist = primes(1000000)
primeset = set(primeslist)
print "Prime List ", len(primeslist)

largestLen = 1
largestSum = 0
for i in range (0, len(primeslist)):
    sum = 0
    listlen = 0
    print "LargestLen: ",  largestLen
    if (len(primesslist)>i+largestLen):
        end = i+largestLen
    else:
        end = len(primeslist) - largestLen

    print "i:", i,"end", end, "maxLen:",largestLen

    for j in range (i, end):
        #print "j:",j, " prime:",primeslist[j]
        sum = primeslist[j]+sum
        print "Preload sum: ", sum, "for length:",largestLen
    first_run = True;
    listlen = largestLen
    if primeslist.count(sum)>0 or first_run:
        if sum > 1000000:
            break;
        print "sum:", sum
        first_run = False;
        for j in range (i+largestLen, len(primeslist)):
            sum = primeslist[j]+ sum
            listlen = listlen + 1
            i
            if sum in primeset:
                if listlen > largestLen:
                    largestLen = listlen
                    largestSum = sum
           

print "Largest Sum ", largestSum, "Largest Length ", largestLen
