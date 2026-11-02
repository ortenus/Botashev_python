n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
d = int(input())
mult = [x * d for x in a]
print(mult)
print(len([x for x in a if x == d]))