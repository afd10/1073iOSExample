
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


primeslist = primes(10000)
primeset = set(primeslist)

workingset = {}
for p in primeslist:
    if p>1000:
        sortIt = ''.join(sorted(str(p)))
        if not(sortIt in workingset):
            workingset[sortIt] = [p]
        else:
            workingset[sortIt].append(p)

for i in workingset.keys():
    if len(workingset[i]) > 2:
        sumset = {} 
        for j in range(0,len(workingset[i])):
            for k in range (1, len(workingset[i])):
                diff = workingset[i][k] - workingset[i][j]
                if diff > 0:
                    if (diff not in sumset):
                        sumset[diff] = [workingset[i][j], workingset[i][k]]
                    else:
                        #print diff, ": ",i, ", ",j, ", ",k
                        sumset[diff].append(workingset[i][j])
                        sumset[diff].append(workingset[i][k])
        for l in sumset.keys():
            if len(sumset[l]) > 3:
                st = sorted(list(set(sumset[l])))
                if (st[0] + 2*l) == st[2]:
                    print l, ": ", st
