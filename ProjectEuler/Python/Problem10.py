def sieve(n, set):
      return filter(lambda x: x % n, set)


newset = range(2,10)
primeList = []

location = 0
current = newset[0]
while (current != newset[-1]):
    newset = sieve(newset[location], newset)
    primeList.append(newset[location])
    print newset
    if current == newset[location]:
        location+=1

print newset
