a = [2, 3, 4, 5, 6]
sum_even_idx = 0
prod_even_idx = 1
for i in range(0, len(a), 2):
    sum_even_idx += a[i]
    prod_even_idx *= a[i]
print(sum_even_idx)
print(prod_even_idx)