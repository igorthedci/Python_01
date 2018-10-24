"""
Записывает в новый файл все слова в алфавитном порядке из другого файла с
текстом. Каждое слово на новой строке.
* (доп.) Рядом со словом укажите сколько раз оно встречалось в тексте
"""


def take_key(elem):
    return elem


def take_value(elem):
    return zdict[elem]


if __name__ == '__main__':
#
    in_file = r"./tmp/zen.py"
    out_file = r'./tmp/f-zen.py'
#   in_handle = open(in_file, encoding='utf-8')
#   out_handle = open(out_file, 'w', encoding='utf-8')
#
    with open(in_file, encoding='utf-8') as in_handle:
        with open(out_file, 'wt', encoding='utf-8') as out_handle:
#
            zdict = {}  # initialize the dictionary
            for aline in in_handle:
                aline = aline.split(' ')
                for aword in aline:  # add all words from a line to the dictionary
                    if aword.isalpha():
                        aword = aword.lower()
                        value = zdict.get(aword)
                        value = 1 if not value else value + 1
                        zdict[aword] = value  # word is key, frequency is value
#
            sort_value = sorted(zdict, key=take_value)
            sort_word = sorted(zdict, key=take_key)
#
            print('\nSorting by words', file=out_handle)
            for item in sort_word:
                print("%2s : %s" % (zdict[item], item), file=out_handle)
            print('\nSorting by frequency', file=out_handle)
            for item in sort_value:
                print("%2s : %s" % (zdict[item], item), file=out_handle)
#
#   in_handle.close()
#   out_handle.close()
