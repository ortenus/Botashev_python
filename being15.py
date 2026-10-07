# Begin15. Дана площадь S круга. Найти его диаметр D и длину L окружности.
area = float(input())
pi = 3.14
radius = (area / pi) ** 0.5
diameter = 2 * radius
length = 2 * pi * radius
print(diameter)
print(length)
