import math

# Задание 1
#
# Входные данные
# Пользователь вводит строку. Выловите исключения, если введённая строка слишком короткая.
# Выходные данные
# Воспользуйтесь одним print(), но при этом выводите с новой строки:
# Сначала выведите третий символ этой строки.
# Во второй строке выведите предпоследний символ этой строки.
# В третьей строке выведите первые пять символов этой строки.
# В четвертой строке выведите всю строку, кроме последних двух символов.
# В пятой строке выведите все символы с четными индексами (считая,
#   что индексация начинается с 0, поэтому символы выводятся, начиная с первого).
# В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
# В седьмой строке выведите все символы в обратном порядке.
# В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
# В девятой строке выведите все символы в обратном порядке без первого и последнего элемента.
# В десятой строке выведите длину данной строки.

sss = input("Enter a string: ")
report = "Исходная строка: " + sss
try :
    report += "\n1. Третий символ строки: " + sss[2:3]
    report += "\n2. Последний символ строки: " + sss[-1]  # sss[-1:-2:-1]
    report += "\n3. Первые пять символов строки: " + sss[0:5]
    report += "\n4. Строка без последних двух символов: " + sss[0:-2]
    report += "\n5. Четные символы: " + sss[1::2]
    report += "\n6. Нечетные символы кроме первого: " + sss[2::2]
    report += "\n7. Строка в обратном порядке: " + sss[::-1]
    report += "\n8. Символы в обратном порядке через один: " + sss[::-2]
    report += "\n9. Символы в обратном порядке без крайних символов: " + sss[-2:1:-2]
    report += "\n10. Длина строки: " + str(len(sss))
except IndexError :
    print("Строка слишком короткая для завершения анализа.")
finally :
    print(report)

# ------------------------------------------------------------------------------------- Задание 2
#
# Пользователь вводит строку.
# Разрежьте её на две равные части (если длина строки — чётная,
# а если длина строки нечётная, то длина первой части должна быть на один символ больше).
# Переставьте эти две части местами, результат запишите в новую строку и выведите на экран.

sss = input("Enter a string: ")
fff = (len(sss) + 1) // 2
ggg = sss[fff:] + sss[:fff]
print(ggg)


# ------------------------------------------------------------------------------------- Задание 3
#
# 1) Напишите счетчик с помощью конструкции while, который выводит числа от 0 до 10.
# 2) Напишите счетчик с помощью конструкции while, который выводит числа от 20 до 1.
# Попробуйте вывести числа в одной строчке, разделённые пробелом

sss = "0"
num = 1
while num < 11 :
    sss += " " + str(num)
    num += 1
print(sss)

sss = "20"
num = 19
while num > 0 :
    sss += " " + str(num)
    num -= 1
print(sss)


# ------------------------------------------------------------ Задание 4
#
# У вас есть список чисел.
# 1. Напишите цикл, который выводит на экран и удаляет с начала элементы списка, пока он не останется пустым
# 2. ** Как сделать это же задание со строкой:
# напишите цикл, который выводит на экран и «удаляет» первый символ строки, пока она не станет пустой?
# 3. Напишите цикл, который выводит на экран и удаляет элементы списка от самого маленького до самого большого,
# пока он не останется пустым.


nnn = [9, 6, 3, 7, 11, 5, 6]
nnn2 = nnn.copy()
print("Исходный список:\n", nnn, "\nУдаление элементов с начала списка:")
while True :
    try :
        print(nnn.pop(0))
    except (IndexError, ValueError) :
        print("Список закончен")
        break

sss = "string"
print("Исходная строка:", sss, "\nУдаление символов с начала строки:")
while True :
    print(sss)
    sss = sss[1:]
    if sss == "" :
        print("Строка закончена")
        break

print("Исходный список:\n", nnn2, "\nУдаление элементов, начиная с минимальных:")
nnn_sort = nnn2.copy()
nnn_sort.sort()
for num in nnn_sort :
    nnn2.remove(num)
    print(nnn2)

# -------------------------------------------------------------------- Задание 5
# Создайте строку, в которой написан, какой-то текст. Пример:
# We are not what we should be!
# We are not what we need to be.
# But at least we are not what we used to be
#  (Football Coach)
# Посчитайте сколько слов в тексте (разбейте на слова методом строк split)
# Удалите знаки препинания (пройдитесь циклом все слова и удалите методом strip знаки препинания)
# Выведите слова в алфавитном порядке (найдите метод списка, который сортирует)
#
# Усложнённое ** (можно сначала его не делать):
# Посчитать, сколько раз встречается каждое слово.
# (Подсказка: создавать словарь, где ключи — это слова из текста,
# а в значениях подсчитываем количество «встречаний» этого слова)


def text_number_of_words(text) :
    ttt = text.split(' ')
    return len(ttt)


def text_without_punctuation(text) :
    ttt = text.strip()
    ttt = ttt.replace("\n", " ")
    ttt = ttt.replace(". ", " ")
    ttt = ttt.replace(" - ", " ")
    ttt = ttt.replace(",", "")
    ttt = ttt.replace("!", "")
    ttt = ttt.replace("?", "")
    ttt = ttt.replace("  ", " ")
    return ttt


def text_dictionary_of_words(text) :
    ttt = text_without_punctuation(text)
    ttt = ttt.split(" ")
    ttt.sort()
    return ttt


def text_frequency_analysis(text) :
    ttt = text_dictionary_of_words(text)
    ddd = {}
    for www in ttt :  # перебрать все слова в списке
        if www.isalnum() and not ddd.get(www) :  # если слово отсутствует в словаре, то...
            qqq = ttt.count(www)  # посчитать количество этих слов в списке
            ddd[www] = qqq  # и добавить в словарь новый элемент
    return ddd


sss = """
Camping is really not my cup of tea 
so I’m going to visit my friend in New York instead.

Don’t trouble yourself cooking such a big meal. I eat like a bird.

My mother has to cook a lot of food when my brother comes to visit. 
He eats like a horse.
    """
print("Исходный текст:\n", sss)
print("Количество слов в тексте:", text_number_of_words(sss))
print("Текст без знаков пунктуации:\n", text_without_punctuation(sss))
print("Словарный состав текста:\n", text_dictionary_of_words(sss))
qqq = text_frequency_analysis(sss)
print("Частотный анализ текста:\n", qqq)
print("Количество уникальных слов:", len(qqq))


# -------------------------------------------------------------------- Задание 6
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


# ----------------------------------------------------------------------------------- Задание 7
# Функция принимает три числа a, b, c.
# Функция должна определить, существует ли треугольник с такими сторонами.
# Eсли треугольник существует, то функция возвращает тип треугольника:
#  Equilateral triangle (равносторонний),
#  Isosceles triangle (равнобедренный),
#  Versatile triangle (разносторонний)
#  или не треугольник (Not a triangle).


def is_triangle(a, b, c):
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
    except (ValueError, TypeError):
        return 0
    if a <= 0 or b <= 0 or c <= 0:
        return 0
    if (a + b) <= c or (b + c) <= a or (c + a) <= b:
        return 0
    if a == b and b == c:
        return 1
    if a == b or b == c or c == a:
        return 2
    return 3


# end of def


def type_triangle(a, b, c):
    ttt = is_triangle(a, b, c)
    sss = "Sides: [ " + str(a) + ", " + str(b) + ", " + str(c) + " ] Shape: "
    if ttt == 1:
        return sss + "Equilateral triangle"
    elif ttt == 2:
        return sss + "Isosceles triangle"
    elif ttt == 3:
        return sss + "Versatile triangle"
    else:
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


# ------------------------------------------------------------------------------- Задание 8
# Оформляем в функции наши задания на уроке:
# 1) Пишем функцию, которая попросит пользователя ввести слово
# (строка без пробелов в середине, а вначале и в конце пробелы могут быть).
# Пока он не введёт правильно, просите его ввести.
# Функция возвращает введённое слово
#
# 2) Пишем функцию, которая попросит ввести число.
# Пока он не введёт правильно, просите его ввести.
# Функция возвращает введённое число.


def inputWord():
    while True:
        ddd = input("Enter a word: ").strip()
        if len(ddd) == 0:
            print("Word is not detected.")
            continue
        elif ' ' not in ddd:
            break
        print(ddd, "contains space(s) inside.")
    print("Thank you!", ddd, "is correct word.")
    return ddd


def inputFloat():
    while True:
        ddd = input("Enter a number: ")
        try:
            rrr = float(ddd)
        except ValueError:
            print(ddd, "is not a valid number.")
            continue
        break
    print("Thank you!", rrr, "is correct number.")
    return rrr
# tests:
#print(inputWord())
#print(inputFloat())
#
# -------------------------------------------------------------------------- Задание 9
# Даны четыре действительных числа: x1, y1, x2, y2.
# Напишите функцию distance(x1, y1, x2, y2), вычисляющую расстояние между точкой (x1, y1) и (x2, y2).
# Считайте четыре действительных числа от пользователя и выведите результат работы этой функции.


def distance_two_dots(x1, y1, x2, y2):
    ddd = (x1 - x2) ** 2
    ddd += (y1 - y2) ** 2
    return math.sqrt(ddd)


x1 = float(input("Enter X1 coordinate: "))
y1 = float(input("Enter Y1 coordinate: "))
x2 = float(input("Enter X2 coordinate: "))
y2 = float(input("Enter Y2 coordinate: "))
ddd = distance_two_dots(x1, y1, x2, y2)
print("Distance between two points is ", ddd)
