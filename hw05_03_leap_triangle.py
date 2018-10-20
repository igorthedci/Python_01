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

class MyYear:

    def __init__(self, year=None):
        self.year = year

    def is_year_leap(self, log=None):
        """
        • Написать функцию is_year_leap, принимающую 1 аргумент — год,
        и возвращающую True, если год високосный, и False иначе.
        :param log == True:  logging is required
        :return: True or False
        """
        result = False
        try:
            year = int(self.year)
        except ValueError:
            result = False
        else:
            if year == 0:
                result = False
            elif year % 400 == 0:
                result = True
            elif year % 100 == 0:
                result = False
            elif year % 4 == 0:
                result = True
        finally:
            if (log):
                print('is_year_leap({}) -> {}'.format(self.year, result))
            return result

    # def run_log(self, proc):
    #     print('{}({}) -> {}'.format(proc, self.args, self.proc()))


class MyTriangle:

    NO_TRIANGLE = 'Not a triangle'
    VERSATILE = 'Versatile triangle'
    ISOSCELES = 'Isosceles triangle'
    EQUILATERAL = 'Equilateral triangle'

    def __init__(self, *args):
        self.args = list(args)

    def is_triangle(self):
        """
         • Функция принимает три числа a, b, c.
        Функция должна определить, существует ли треугольник с такими сторонами.
        Если треугольник существует, вернёт True, иначе False.
        :param args:
        :return:
        """
    #    print(args, len(args), type(args))
        if len(self.args) < 3:
            return False
        try:
            a, b, c = int(self.args[0]), int(self.args[1]), int(self.args[2])
        except ValueError:
            return False
    #    print(a, b, c)
        if a <= 0 or b <= 0 or c <= 0:
            return False
        if (a >= b + c) or (b >= c + a) or (c >= a + b):
            return False
        return True

    def type_triangle(self):
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
        if not self.is_triangle():
            return self.NO_TRIANGLE
        a, b, c = int(self.args[0]), int(self.args[1]), int(self.args[2])
        if a == b == c:
            return self.EQUILATERAL
        if a != b != c != a:
            return self.VERSATILE
        return self.ISOSCELES

    # def run_log(self, proc):
    #     print('{}({}) -> {}'.format(proc, self.args, MyTriangle().proc()))


if __name__ == '__main__':
#
    MyYear().is_year_leap(log=True)
    MyYear('a').is_year_leap(log=True)
    MyYear(0).is_year_leap(log=True)
    MyYear(-1).is_year_leap(log=True)
    MyYear(-4).is_year_leap(log=True)
    MyYear(1).is_year_leap(log=True)
    MyYear(4).is_year_leap(log=True)
    MyYear(100).is_year_leap(log=True)
    MyYear(400).is_year_leap(log=True)
    MyYear(2000).is_year_leap(log=True)
    MyYear(2000).is_year_leap()
#
    print('is_triangle({}) -> {}'.format('a', MyTriangle('a').is_triangle()))
    print('is_triangle({}) -> {}'.format(1, MyTriangle(1).is_triangle()))
    print('is_triangle({}) -> {}'.format((1, 1, 0), MyTriangle(1, 1, 0).is_triangle()))
    print('is_triangle({}) -> {}'.format((1, 1, -1), MyTriangle(1, 1, -1).is_triangle()))
    print('is_triangle({}) -> {}'.format((1, 1, 3), MyTriangle(1, 1, 3).is_triangle()))
    print('is_triangle({}) -> {}'.format((1, 1, 1), MyTriangle(1, 1, 1).is_triangle()))
#
    print('type_triangle({}) -> {}'.format((1, 1, 3), MyTriangle(1, 1, 3).type_triangle()))
    print('type_triangle({}) -> {}'.format((1, 1, 1), MyTriangle(1, 1, 1).type_triangle()))
    print('type_triangle({}) -> {}'.format((1, 2, 2), MyTriangle(1, 2, 2).type_triangle()))
    print('type_triangle({}) -> {}'.format((4, 3, 2), MyTriangle(4, 3, 2).type_triangle()))
