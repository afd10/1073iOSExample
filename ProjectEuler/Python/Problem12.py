from math import sqrt,ceil

def find_factors(n):
    factors = []
    for i in range(2,int(ceil(sqrt(n)))):
        if n%i==0:
            factors.append(i)
    return factors

fact_count = 0
count = 2
sum = 1
while fact_count < 250:
    sum += count
    count += 1
    fact_count = len(find_factors(sum))

print sum


