
global89= set([])
global1 = set([])

def sdc(n):
    """$ find the square digit chain """
    #print "->", n
    digs = map(int, str(n))
    sdcsum =  sum([x**2 for x in map(int, digs)])
    if sdcsum ==1 or sdcsum == 89:
        #print 
        return sdcsum
    else: 
        #print sdcsum
        s =sdc(sdcsum)
        return s

def sdc2(n):
    """$ find the square digit chain """
    #print "->", n
    if n in global89:    
        return 89
    if n in global1:
        return 1
    
    digs = map(int, str(n))
    sdcsum =  sum([x**2 for x in map(int, digs)])
    if sdcsum ==1:         #print 
        global1.add(n)
        return sdcsum
    if sdcsum == 89:
        global89.add(n)
        return sdcsum

    else: 
        #print sdcsum
        s =sdc(sdcsum)
        return s



print sdc(44)
print sdc(85)

encnt = 0
for i in range(1,10000000):
    if sdc2(i) == 89:
        encnt = encnt + 1

print encnt
print len(global89)
