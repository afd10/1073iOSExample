
constant = ""
for i in range(0, 1000000):
    constant+=str(i)

print 1, int(constant[1])
print 12, int(constant[12])
print 10, int(constant[10])
print 100, int(constant[100])
print 1000, int(constant[1000])
print 10000, int(constant[10000])
print 100000,int(constant[100000])
print 1000000, int(constant[1000000])
prod =  int(constant[1]) * int(constant[10]) * int(constant[100]) * int(constant[1000]) * int(constant[10000]) * int(constant[100000]) * int(constant[1000000])

print prod
