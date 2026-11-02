n = int(input())
rest = n
while rest % 3 == 0 and rest > 1:
    rest //= 3
print(rest == 1)