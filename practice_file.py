from math import sqrt, pi
# def absolute_value(x): 
#     if x ==0: 
#         return 0
#     elif x > 0:
#         return x
#     elif x < 0: 
#         return -x 
#     else :
#         return 'error'
    
# print(absolute_value(0))
# print(absolute_value(-1))
# print(absolute_value(2))

# def fib_seq(n): 
#     k = 1
#     previous, current = 1,0
#     if n == 0:
#         return 0
#     else: 
#         while k < n:
#             previous, current = current, previous + current
#             k +=1
#         return current

# print(fib_seq(5)) # // 3
# print(fib_seq(4)) # // 2
# print(fib_seq(3)) # // 1
# print(fib_seq(8)) ## 13

def area (r, shape_constant): 
    assert r > 0, 'The length must be greater than 0'
    return r ** 2 * shape_constant

def area_square (r):
    return area(r,1)

def area_hexagon (r):
    return area(r, 3 * sqrt(3) / 2)

def area_sphere (r):
    return area(r, pi)
print(area_square(9))
print(area_sphere(9))
print(area_hexagon(9))
print(3 * sqrt(3) / 2)