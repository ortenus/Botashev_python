def shift_left3(a, b, c):
    return b, c, a
for i in range(2):
    a = float(input())
    b = float(input())
    c = float(input())
    res_a, res_b, res_c = shift_left3(a, b, c)
    print(res_a)
    print(res_b)
    print(res_c)