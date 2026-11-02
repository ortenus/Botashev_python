a = [10, 20, 30, 40, 50]
avg = sum(a) / len(a)
greater_than_avg = [x for x in a if x > avg]
print(avg)
print(greater_than_avg)
print(len(greater_than_avg))
