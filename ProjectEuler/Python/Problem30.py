

def sumdigits(n):
    listn  = map(int, str(n))
    sqlist = (x**5 for x in listn)
    sumn = sum(sqlist)
    #print listn, sqlist
    return sumn

fifthpower = []
for i in range(1000, 1000000):
    if sumdigits(i) == i:
        fifthpower.append(i)
        print i
print ">>", sum(fifthpower)
