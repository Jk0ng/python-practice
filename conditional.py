
def absolute_value(x): 
    """The function to return the absolute value of an number, the number could be +/- or zero"""
    if x == 0:
        return 0 
    elif x > 0:
        return x
    elif x < 0: 
        return - x 
    else: 
        return 'error'
    
print(absolute_value(-9))
print(absolute_value(9))
print(absolute_value(0))

def fibonacci(n): 
    """find the number at nth fibonacci sequence"""
    prev, curr = 1,0
    k = 1    
    while k < n:
        prev, curr = curr, prev + curr
        k = k + 1
    return curr

print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))
print(fibonacci(0))

