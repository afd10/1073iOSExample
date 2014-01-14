rangeA = range(2,101);
rangeB = range(2,101);

powlist = []

for a in rangeA:
    for b in rangeB:
        powlist.append(a**b)

result_set = set(powlist)
print len(result_set)
#print result_set

