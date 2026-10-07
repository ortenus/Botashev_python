# Begin6. Даны длины ребер a, b, c прямоугольного параллелепипеда. Найти объем V и площадь S.
a = float(input())
b = float(input())
c = float(input())
volume = a * b * c
surface = 2 * (a * b + b * c + a * c)
print(volume)
print(surface)
