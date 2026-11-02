def rect_ps(x1, y1, x2, y2):
    width = abs(x1 - x2)
    height = abs(y1 - y2)
    p = 2 * (width + height)
    s = width * height
    return p, s
for i in range(3):
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    perimeter, area = rect_ps(x1, y1, x2, y2)
    print(perimeter)
    print(area)