#
# Задание 6
# Это уже было, но теперь оформите это функцией:
# 1) Написать функцию is_year_leap, принимающую 1 аргумент — год,
# и возвращающую True, если год високосный, и False иначе.
# 2) Функция принимает три числа a, b, c.
# Функция должна определить, существует ли треугольник с такими сторонами.
# Если треугольник существует, вернёт True, иначе False.


def is_year_leap(year) :
    """
Return:
True = the year it LEAP
False = the year it NOT LEAP
    """
    try:
        year = int(year)
    except (ValueError, TypeError) :
        return False
    condition = (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)
    return condition
# end of def


# asserts:
print(is_year_leap(None))
print(is_year_leap("q"))
print(is_year_leap("-1.1"))
print(is_year_leap(0))
print(is_year_leap(2000))
print(is_year_leap(2100))
print(is_year_leap(2111))
