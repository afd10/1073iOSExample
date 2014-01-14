spiralsize = 1001
last = (spiralsize -3)/2

print "last:",last;
corners = [1,1,1,1]
sum = 1
for i in range(0,last+1):
    for j in range(0, len(corners)):
        print "j:", j," offset:", ((j+1)*2), "i: ",i
        corners[j] = corners[j] + ((j+1)*2)+(8*i)
        sum = sum + corners[j] 
    print corners
print "sum: ",sum
