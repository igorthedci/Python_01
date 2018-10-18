# Задание 8
# Оформляем в функции наши задания на уроке:
# 1) Пишем функцию, которая попросит пользователя ввести слово
# (строка без пробелов в середине, а вначале и в конце пробелы могут быть).
# Пока он не введёт правильно, просите его ввести.
# Функция возвращает введённое слово
#
# 2) Пишем функцию, которая попросит ввести число.
# Пока он не введёт правильно, просите его ввести.
# Функция возвращает введённое число.
#
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
#
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
