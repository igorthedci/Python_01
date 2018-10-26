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
    with open(in_file, encoding='utf-8') as in_handle:
        with open(out_file, 'wt', encoding='utf-8') as out_handle:
            aline = in_handle.readline()
            titles = aline.split(' ')
            arr_person = []
            for aline in in_handle:
                aline = aline.split(' ')
                arr_person.append( { aline[0]+'_'+aline[1] : (aline[2], aline[3]) } )
#
            arr_dept = []  # item of the array = {title : person_with_max_salary}
            for aperson in arr_person:

                if aperson[2] in arr_dept:
                    if
                else:
                    arr_dept.append((aperson[2],aperson[3]))
