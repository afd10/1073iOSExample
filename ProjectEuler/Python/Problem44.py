
def pentagonal(n):
    return n* (3*n-1)/2

worklist = []
for i in range(0,10000):
    worklist.append(pentagonal(i))

workset = set(worklist)

diflist = []
for i in range(1,len(worklist)):
    for j in range (1, len(worklist)):
        if (worklist[i] + worklist[j]) in workset:
            if  (worklist[j] - worklist[i]) in workset:
                diflist.append(worklist[j] - worklist[i])
                print "minus: ", worklist[i], " + ", worklist[j]

print diflist
