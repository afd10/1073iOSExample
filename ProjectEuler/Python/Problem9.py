from math import sqrt

squares = map(lambda x: x * x, range(1,997))

for a in squares:
    for b in squares:
        if (a + b) in squares:
            print "%d\t%d\t%d" %(a, b, a+b)
            if (sqrt(a) + sqrt(b) + sqrt(a+b) == 1000):
                print "Winner! ", sqrt(a) * sqrt(b) *sqrt(a+b)
                exit()


