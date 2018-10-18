import math
#
# Задания 9
# Даны четыре действительных числа: x1, y1, x2, y2.
# Напишите функцию distance(x1, y1, x2, y2), вычисляющую расстояние между точкой (x1, y1) и (x2, y2).
# Считайте четыре действительных числа от пользователя и выведите результат работы этой функции.
#
def distance_two_dots(x1, y1, x2, y2):
    ddd = (x1 - x2) ** 2
    ddd += (y1 - y2) ** 2
    return math.sqrt(ddd)

if __name__ == "__main__":
    x1 = float(input("Enter X1 coordinate: "))
    y1 = float(input("Enter Y1 coordinate: "))
    x2 = float(input("Enter X2 coordinate: "))
    y2 = float(input("Enter Y2 coordinate: "))
    ddd = distance_two_dots(x1, y1, x2, y2)
    print("Distance between two points is ", ddd)
