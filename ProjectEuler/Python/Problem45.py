
def triangle(n):
    return n * (n+1)/2

def pentagonal(n):
    return n* (3*n-1)/2

def hexagonal(n):
    return n*(2*n-1)

triset = set()
pentset = set()
hexset = set()
for i in range(2,1500000):
    triset.add(triangle(i))
    pentset.add(pentagonal(i))
    hexset.add(hexagonal(i))

print set.intersection(triset, pentset, hexset)
