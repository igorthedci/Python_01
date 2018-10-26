"""
Файл имеет вид таблицы: Фамилия Имя Отдел Зарплата
(В первой строке заголовки колонок)
 Посчитайте сколько отделов на фирме
 Определите максимальную зарплату
 Определите максимальную зарплату в каждом отделе
 Выведите «Отдел Макс_Зарплата  Фамилия_человека_с_такой_зарплатой» в новый файл
"""


if __name__ == '__main__':
#
    in_file = r"./tmp/_salary.txt"
    out_file = r'./tmp/_salary_report.txt'
#       in_handle = open(in_file, encoding='utf-8')
#      out_handle = open(out_file, 'w', encoding='utf-8')
#
    arr_person = []  # item = { id: Имя_Фамилия, dept: Отдел, salary: Зарплата }
    with open(in_file, encoding='utf-8') as in_handle:
        aline = in_handle.readline()
        titles = aline.split(' ')
        key_id = titles[1] + '_' + titles[0]
        key_dept = titles[2]
        key_salary = titles[3]
        for aline in in_handle:
            aline = aline.split(' ')
            arr_person.append( { key_id: aline[1]+'_'+aline[0], key_dept: aline[2], key_salary: aline[3] } )
# 1 Посчитайте сколько отделов на фирме
    arr_dept = []  # item = { id: counter, title: Отдел }
    for aperson in arr_person:

            arr_dept = []  # item of the array = {title : person_with_max_salary}
            for aperson in arr_person:

                if aperson[2] in arr_dept:
                    if
                else:
                    arr_dept.append((aperson[2],aperson[3]))

        with open(out_file, 'wt', encoding='utf-8') as out_handle:
