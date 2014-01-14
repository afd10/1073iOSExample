from math import sqrt, ceil

def abundant(n):
    factors = set([1])
    for i in range(2,int((ceil(sqrt(n))))+1):
        if (n%i == 0):
            factors.add(i);
            #if sqrt(n) != i:
            factors.add(n/i);
    sumfact = sum(factors)
    print n, " : ", factors, " : ",sumfact
    if sumfact > n:
        print ">", n, " : ", factors, " : ",sumfact
        return True
    return False
    
print "START"
abundants = []
for i in range (12,28124):
    if abundant(i):
        abundants.append(i)

print "abundant list:", abundants

abundantsums = []
for i in range(0,len(abundants)):
    for j in range( 0, len(abundants)):
        absum = abundants[i] + abundants[j]
        #if absum < 28123:
        abundantsums.append(absum)

allints = range(1,28124)
setints = set(allints)

setAS = set(abundantsums)
print "absums:", len(abundantsums)
print "SETAS:", len(setAS)

nonabints = setints - setAS
print sorted(nonabints)
final = sum(nonabints)
print "Final: ",final
