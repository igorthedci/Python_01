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
import unittest
from hw05_03_leap_triangle import MyYear, MyTriangle


class LeapYearTests(unittest.TestCase):
    """
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
    """
    def test_01(self):
        self.assertEqual(False, MyYear().is_year_leap())

    def test_02(self):
        self.assertEqual(False, MyYear('a').is_year_leap())

    def test_03(self):
        self.assertEqual(False, MyYear(0).is_year_leap())

    def test_04(self):
        self.assertEqual(False, MyYear(-1).is_year_leap())

    def test_05(self):
        self.assertEqual(True, MyYear(-4).is_year_leap())

    def test_06(self):
        self.assertEqual(False, MyYear(1).is_year_leap())

    def test_07(self):
        self.assertEqual(True, MyYear(4).is_year_leap())

    def test_08(self):
        self.assertEqual(False, MyYear(100).is_year_leap())

    def test_09(self):
        self.assertEqual(True, MyYear(400).is_year_leap())

    def test_10(self):
        self.assertEqual(True, MyYear(2000).is_year_leap())


class IsTriangleTests(unittest.TestCase):
    """
    print('is_triangle({}) -> {}'.format(('a'), is_triangle('a')))
    print('is_triangle({}) -> {}'.format((1), is_triangle(1)))
    print('is_triangle({}) -> {}'.format((1, 1, 0), is_triangle(1, 1, 0)))
    print('is_triangle({}) -> {}'.format((1, 1, -1), is_triangle(1, 1, -1)))
    print('is_triangle({}) -> {}'.format((1, 1, 3), is_triangle(1, 1, 3)))
    print('is_triangle({}) -> {}'.format((1, 1, 1), is_triangle(1, 1, 1)))
    """
    def test_01(self):
        self.assertEqual(False, MyTriangle().is_triangle())
        self.assertEqual(False, MyTriangle('a').is_triangle())
        self.assertEqual(False, MyTriangle(1).is_triangle())
        self.assertEqual(False, MyTriangle(1, 1, 0).is_triangle())
        self.assertEqual(False, MyTriangle(1, 1, -1).is_triangle())
        self.assertEqual(False, MyTriangle(1, 1, 3).is_triangle())
        self.assertEqual(True, MyTriangle(1, 1, 1).is_triangle())


class TypeTriangleTests(unittest.TestCase):
#
    NO_TRIANGLE = 'Not a triangle'
    VERSATILE = 'Versatile triangle'
    ISOSCELES = 'Isosceles triangle'
    EQUILATERAL = 'Equilateral triangle'
    """
    print('type_triangle({}) -> {}'.format((1, 1, 3), type_triangle(1, 1, 3)))
    print('type_triangle({}) -> {}'.format((1, 1, 1), type_triangle(1, 1, 1)))
    print('type_triangle({}) -> {}'.format((1, 2, 2), type_triangle(1, 2, 2)))
    print('type_triangle({}) -> {}'.format((4, 3, 2), type_triangle(4, 3, 2)))
    """
    def test_01(self):
        self.assertEqual(self.NO_TRIANGLE, MyTriangle(1, 1, 3).type_triangle())
        self.assertEqual(self.EQUILATERAL, MyTriangle(1, 1, 1).type_triangle())
        self.assertEqual(self.ISOSCELES, MyTriangle(1, 2, 2).type_triangle())
        self.assertEqual(self.VERSATILE, MyTriangle(4, 3, 2).type_triangle())


if __name__ == '__main__':
    pass
#
#
