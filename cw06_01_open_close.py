
def play_line(leng=3, endcode=0):
    """
# Функция генерирует строку la-la-la.
# Функция принимает 1 аргумент:
# 1-е число – сколько «la» будет в строке («la» в строке объединяются дефисом). По умолчанию 3
    """
    line = 'la'
    for i in range(leng - 1):
        line += '-la'
    # line = ['la' for i in range(leng)]
    # print(*line, sep='-')
    return line


if __name__ == '__main__':
    handle = open(r".\tmp\cw06_02.txt", "a")
    aline = play_line(leng=9)
    handle.write(str(aline)+'\n')
    handle.write(str(aline)+'\n')
    handle.close()
    pass
    # handle = open(r".\hw05_01_persons.py", 'r', encoding='utf-8')
    # atext = handle.readlines()
    # for i in (range(len(atext))):
    #     print(atext[i], end='')
    # handle.close()
# добавляем восклицательный знак в конец строки
    handle = open(r".\hw05_01_persons.py", 'r', encoding='utf-8')
    for line in handle:
        print(line[:-2] + '!')
        # print(line.strip() + '!')
    handle.close()
# перевернуть строку
    handle = open(r".\hw05_01_persons.py", 'r', encoding='utf-8')
    for line in handle:
        print(line[-2::-1]+'!')
    handle.close()
#
