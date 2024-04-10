def absolute_value(x): 
    """Return the absolute value of x"""
    if x > 0:
        return x
    elif x < 0:
        return -x
    else: 
        return 0
    
print(absolute_value(-9))
print(absolute_value(9))
print(absolute_value(0))

def fib(n):
    """Find the Nth fibonacci number"""
    prev, curr=0,1
    k = 1 
    while k < n:
        prev, curr= curr, curr + prev
        k = k + 1
    return curr 
print(fib(5))
print(fib(6))
print(fib(7))
print(fib(8))