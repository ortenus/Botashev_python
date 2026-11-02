a = [3, 5, 7, 5, 9, 5]
d = 5
count = a.count(d)
if d in a:
    first_index = a.index(d)
else:
    first_index = -1
print(count)
print(first_index)
