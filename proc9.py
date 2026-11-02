def add_left_digit(d, k):
    count = 0
    temp = k
    if temp == 0:
        count = 1
    while temp > 0:
        count += 1
        temp //= 10
    return d * (10**count) + k
k = int(input())
d1 = int(input())
d2 = int(input())
k = add_left_digit(d1, k)
print(k)
k = add_left_digit(d2, k)
print(k)
