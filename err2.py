a = int(input())
b = int(input())

try:
    print(a / b)
except ZeroDivisionError:
    print("Делить на ноль нельзя")