#
# Задание 7
# Функция принимает три числа a, b, c.
# Функция должна определить, существует ли треугольник с такими сторонами.
# Eсли треугольник существует, то функция возвращает тип треугольника:
#  Equilateral triangle (равносторонний),
#  Isosceles triangle (равнобедренный),
#  Versatile triangle (разносторонний)
#  или не треугольник (Not a triangle).


def is_triangle(a, b, c) :
    """
Return:
0 = not a triangle
1 = Equilateral
2 = Isosceles
3 = Versatile
    """
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except (ValueError, TypeError) :
        return 0
    if a <= 0 or b <= 0 or c <= 0 :
        return 0
    if (a + b) <= c or (b + c) <= a or(c + a) <= b :
        return 0
    if a == b and b == c :
        return 1
    if a == b or b == c or c == a :
        return 2
    return 3
# end of def


def type_triangle(a, b, c) :
    ttt = is_triangle(a, b, c)
    sss = "Sides: [ " + str(a) + ", " + str(b) + ", " + str(c) + " ] Shape: "
    if ttt == 1 :
        return sss + "Equilateral triangle"
    elif ttt == 2 :
        return sss + "Isosceles triangle"
    elif ttt == 3 :
        return sss + "Versatile triangle"
    else :
        return sss + "not a triangle"
# end of def


# asserts:
print(type_triangle(1, 1, None))
print(type_triangle(1, 1, "a"))
print(type_triangle(1, 1, "0"))
print(type_triangle(1, 1, "-2"))
print(type_triangle(1, 1, "2"))
print(type_triangle(1, 1, "1.5"))
print(type_triangle(1, 1, 1))
print(type_triangle(2, 3, 4))