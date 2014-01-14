def next_fib(a,b):
    return a + b

def is_even(n):
    return (n%2 == 0)

fibminus1 = 1
fib = 2

total = 0
while fib<4000000:
    if (is_even(fib)):
        total = total + fib
    newfib = next_fib(fib, fibminus1)
    fibminus1 = fib
    fib = newfib

print total
