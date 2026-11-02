import math

def triangle_ps(a):
    p = 3 * a
    s = (a**2) * math.sqrt(3) / 4
    return p, s
for i in range(3):
    side = float(input())
    perimeter, area = triangle_ps(side)
    print(perimeter)
    print(area)