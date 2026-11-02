def sort_dec3(a, b, c):
    if a < b:
        a, b = b, a
    if b < c:
        b, c = c, b
    if a < b:
        a, b = b, a
    return a, b, c
for i in range(2):
    x = float(input())
    y = float(input())
    z = float(input())
    res_a, res_b, res_c = sort_dec3(x, y, z)
    print(res_a)
    print(res_b)
    print(res_c)
