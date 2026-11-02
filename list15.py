a = [10, 20, 30, 40, 50, 60]
odd_pos_elements = []
for i in range(1, len(a), 2):
    odd_pos_elements.append(a[i])
total = sum(odd_pos_elements)
print(odd_pos_elements)
print(total)
