"""
Задание 3 (на создание тестов c помощью unittest)

Создайте наборы тестов на написанные функции из прошлого домашнего задания:
    • Написать функцию is_year_leap, принимающую 1 аргумент — год,
    и возвращающую True, если год високосный, и False иначе.
    • Функция принимает три числа a, b, c.
    Функция должна определить, существует ли треугольник с такими сторонами.
    Если треугольник существует, вернёт True, иначе False.
    • Функция принимает три числа a, b, c.
    Функция должна определить, существует ли треугольник с такими сторонами и если существует,
    то возвращает тип треугольника Equilateral triangle (равносторонний),
    Isosceles triangle (равнобедренный),
    Versatile triangle (разносторонний)
    или не треугольник (Not a triangle).
"""


def is_year_leap(year):
    """
    • Написать функцию is_year_leap, принимающую 1 аргумент — год,
    и возвращающую True, если год високосный, и False иначе.
    :param year:
    :return:
    """
    try:
        year = int(year)
    except ValueError:
        return False
    if year == 0:
        return False
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def is_triangle(*args):
    """
     • Функция принимает три числа a, b, c.
    Функция должна определить, существует ли треугольник с такими сторонами.
    Если треугольник существует, вернёт True, иначе False.
    :param args:
    :return:
    """
#    print(args, len(args), type(args))
    if len(args) < 3:
        return False
    try:
        a, b, c = int(args[0]), int(args[1]), int(args[2])
    except ValueError:
        return False
#    print(a, b, c)
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if (a >= b + c) or (b >= c + a) or (c >= a + b):
        return False
    return True

def type_triangle(*args):
    """
    Функция принимает три числа a, b, c.
    Функция должна определить, существует ли треугольник с такими сторонами и если существует,
    то возвращает тип треугольника Equilateral triangle (равносторонний),
    Isosceles triangle (равнобедренный),
    Versatile triangle (разносторонний)
    или не треугольник (Not a triangle).
    :param args:
    :return:
    """
    NO_TRIANGLE = 'Not a triangle'
    VERSATILE = 'Versatile triangle'
    ISOSCELES = 'Isosceles triangle'
    EQUILATERAL = 'Equilateral triangle'
#
    if not is_triangle(*args):
        return NO_TRIANGLE
    a, b, c = int(args[0]), int(args[1]), int(args[2])
    if a == b == c:
        return EQUILATERAL
    if a != b != c != a:
        return VERSATILE
    return ISOSCELES

# def run_log(proc, *args):


if __name__ == '__main__':
#
    print('is_year_leap({}) -> {}'.format(0, is_year_leap(0)))
    print('is_year_leap({}) -> {}'.format(-1, is_year_leap(-1)))
    print('is_year_leap({}) -> {}'.format(1, is_year_leap(1)))
    print('is_year_leap({}) -> {}'.format(4, is_year_leap(4)))
    print('is_year_leap({}) -> {}'.format(100, is_year_leap(100)))
    print('is_year_leap({}) -> {}'.format(400, is_year_leap(400)))
    print('is_year_leap({}) -> {}'.format(2000, is_year_leap(2000)))
#
    print('is_triangle({}) -> {}'.format(('a'), is_triangle('a')))
    print('is_triangle({}) -> {}'.format((1), is_triangle(1)))
    print('is_triangle({}) -> {}'.format((1, 1, 0), is_triangle(1, 1, 0)))
    print('is_triangle({}) -> {}'.format((1, 1, -1), is_triangle(1, 1, -1)))
    print('is_triangle({}) -> {}'.format((1, 1, 3), is_triangle(1, 1, 3)))
    print('is_triangle({}) -> {}'.format((1, 1, 1), is_triangle(1, 1, 1)))
#
    print('type_triangle({}) -> {}'.format((1, 1, 3), type_triangle(1, 1, 3)))
    print('type_triangle({}) -> {}'.format((1, 1, 1), type_triangle(1, 1, 1)))
    print('type_triangle({}) -> {}'.format((1, 2, 2), type_triangle(1, 2, 2)))
    print('type_triangle({}) -> {}'.format((4, 3, 2), type_triangle(4, 3, 2)))
