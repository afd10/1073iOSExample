
f = open('words.txt', 'r')

def triangle(n):
    return n * (n+1)/2

def stringToNumber(word):
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    newlist = list(word)
    val = 0
    for i in newlist:
        val = alphabet.index(i) + 1 + val
    return val


triset = set()
for i in range (0,1000):
    triset.add(triangle(i))

#print stringToNumber('sky')

count = 0


for line in f:
    if stringToNumber(line.rstrip()) in triset:
        count = count + 1
print "Count ->", count
