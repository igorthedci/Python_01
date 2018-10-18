#
# Задание 5
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

