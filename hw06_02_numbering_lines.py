"""
Задание из класса «Записываем “Number: строка из файла” из одного файла в
другой»:
1. Кто не успел доделываем / тем, кто успел: воспользуйтесь другим способом
для записи в файл (кто сделал с помощью методов – делают с помощью print,
кто сделал с помощью print – делают с помощью методов)
2. Воспользуйтесь менеджером контекста для файла (with ... as), в который вы
записываете информацию.
"""

if __name__ == '__main__':
#
    in_file = r"./distance.py"
    out_file = r'./tmp/distance.py'
#   in_handle = open(in_file, encoding='utf-8')
#   out_handle = open(out_file, 'w', encoding='utf-8')
#
    with open(in_file, encoding='utf-8') as in_handle:
        with open(out_file, 'wt', encoding='utf-8') as out_handle:
#
            i = 1
            for aline in in_handle:
                print("%3s : %s" % (i, aline), end='', file=out_handle)
                i += 1
#
#   in_handle.close()
#   out_handle.close()
