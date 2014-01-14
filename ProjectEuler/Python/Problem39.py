
def findRT(n):
    result = []
    for i in range (1, n/2):
        for j in range(1, n/2):
            k = n - (i + j)
            if (i**2 + j **2 == k**2):
                 #print i, j ,k
                 result.append([i,j,k])
    return result

print findRT(120)

rtdict = {}
for i in range (1,1000):
    print i
    rtdict[i] = len(findRT(i))

max =0
for k in rtdict:
    if rtdict[k] > max:
        print k
        max = rtdict[k]



