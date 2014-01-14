
def swap(array, init, final):
    temp = array[final]
    array[final] = array[init]
    array[init] = temp
    return array


def mutate(array):
    result = []
    for i in range(0,len(array)):
        for j in range(0,len(array)):
            print "i:", i, " j:",j
            res = swap(array,i,j)
            tmp = ''.join(map(str, res))
            result.append(tmp)
    print result
    return result


        


orderedset = set([0,1,2,3,4,5,6,7,8,9])
runlist = []
#ordered = [0,1,2,3]

#fullres = mutate(ordered)
#print "fullres: ",fullres
#print "setfullres:" ,set(fullres)
#sortres = sorted(list(set(fullres)))
#print sortres
 
for i in range (123456789, 9876543210):
    if len((list(str(i)) & orderedset)) >8:
        print i

#print list(str(123456dd))


