from math import factorial

def factdigits(n):
    listn  = map(int, str(n))
    faclist = (factorial(x) for x in listn)
    sumn = sum(faclist)
    #print listn, sqlist
    return sumn

facts = []
for i in range(3, 1000000):
    if factdigits(i) == i:
        facts.append(i)
        print i
print ">>", sum(facts)
