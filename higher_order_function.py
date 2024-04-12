# generalization
from math import pi, sqrt

def area(r, shape_constant):
    assert r > 0, 'The length must be positive'
    return r * r * shape_constant
def area_square (r): 
    return area(r, 1) 


def area_sphere (r):
    return area(r, pi) 

def area_hexagon(r): 
    return area(r, 3 * sqrt(3) / 2)

print(area_square(9))
print(area_sphere(9))
print(area_hexagon(9))
