coincount = 0
for p1 in range(0,201):
    for p2 in range(0,201,2):
        if (p1 + p2 < 200):
            for p5 in range (0,201,5):
                if (p1 + p2 +p5 < 200):
                    for p10 in range (0, 201,10):
                        if (p1 + p2 + p5 + p10 > 190):
                            for p20 in range(0,201,20):
                                for p50 in range (0,201,50):
                                    for p100 in range (0,201,100):
                                        for p200 in range(0,201,200):
                                            if (p1 + p2 + p5 + p10 + p20 + p50+ p100 + p200 ==200):
                                                coincount = coincount + 1
                                                print p1," + ",p2," + ",p5," + ",p10," + ",p20," + ",p50," + ",p100," + ",p200 

print "Coincount: ",coincount

firstRun= """
200  +  0  +  0  +  0  +  0  +  0  +  0  +  0
Coincount:  73682

real	219m41.543s
user	101m29.117s
sys	0m7.224s
"""
