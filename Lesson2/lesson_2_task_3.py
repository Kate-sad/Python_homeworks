import math


def square(side):
    return math.ceil(side * side)


square_side = int(input("Введите сторону кадрата: "))
print(f"Площадь квадрата: {square(square_side)}")
