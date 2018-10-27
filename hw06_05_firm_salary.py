import random
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
#
# 0. генератор сотрудников
    counter = 20  # количество сотрудников
    titles = ['Фамилия', 'Имя', 'Отдел', 'Зарплата']
    titles = " ".join(str(x) for x in titles)
    with open(in_file, 'wt', encoding='utf-8') as in_handle:
        print(str(titles), file=in_handle)
        for i in range(counter):
            lastname = 'Name_' + str(random.randrange(100))
            firstname = 'Name_' + str(random.randrange(101,120))
            dept = 'Department_' + str(random.randrange(10))
            salary = random.randrange(2000, 8000)
            print(lastname, firstname, dept, salary, file=in_handle)
#
    with open(out_file, 'wt', encoding='utf-8') as out_handle:
        print('Homework_06_05', file=out_handle)
#        out_handle.close()
#       in_handle = open(in_file, encoding='utf-8')
#      out_handle = open(out_file, 'w', encoding='utf-8')
#
#  чтение исходных данных
    name_dept = []  # item = {Имя_Фамилия: Отдел} }
    name_salary = []  # item = {Имя_Фамилия: Зарплата} }
    with open(in_file, encoding='utf-8') as in_handle:
        aline = in_handle.readline().strip()
        titles = aline.split(' ')
        # key_id = titles[1] + '_' + titles[0]
        # key_dept = titles[2]
        # key_salary = titles[3]
        # print(key_id, key_dept, key_salary)
        for aline in in_handle:
            aline = aline.strip().split(' ')
            aname = aline[1] + '_' + aline[0]  # key = Имя_Фамилия
            name_dept.append( {aname: aline[2]} )
            name_salary.append( {aname: aline[3]} )
#
# 1 Посчитайте сколько отделов на фирме
    arr_dept = []  # item = [ Отдел ]
    for adept in name_dept:
        print(adept)
        dept = list(adept.values())[0]
        if adept not in arr_dept:
            arr_dept.append(adept)
#
    with open(out_file, 'a', encoding='utf-8') as out_handle:
        print("Количество отделов :", len(arr_dept), file=out_handle)
        counter = 0
        for adept in arr_dept:
            print(counter+1, dept, file=out_handle)
            counter += 1
#
# 2 Определите максимальную зарплату
    salary_max = 0
    for aname in name_salary:
        asalary = int(list(aname.values())[0])
        if salary_max < asalary:
            salary_max = asalary
#
    with open(out_file, 'a', encoding='utf-8') as out_handle:
        print("\nМаксимальная зарплата на фирме :", salary_max, file=out_handle)
#
# 3 Определите максимальную зарплату в каждом отделе
# 4 Выведите «Отдел Макс_Зарплата  Фамилия_человека_с_такой_зарплатой» в новый файл
# (составляется список {отдел : сотрудник_с максимальной_зарплатой}
    dept_maxname = []  # item = { key: dept, value: Имя_Фамилия_с_макс_зарплатой }
    for aname in name_dept:
        aname = list(aname.keys())[0]
        adept = name_dept[aname]
        asalary = int(name_salary[aname])
        print(aname, adept)
        if adept in dept_maxname:
            maxname = dept_maxname[adept]
            maxsalary = int(name_salary[maxname])
            if asalary > maxsalary:
                dept_maxname[adept] = aname
        else:
            dept_maxname.append( {adept: aname} )
#
# 4 Выведите «Отдел Макс_Зарплата  Фамилия_человека_с_такой_зарплатой» в новый файл
    with open(out_file, 'a', encoding='utf-8') as out_handle:
        print("\nМаксимальная зарплат по отделам", file=out_handle)
        counter = 0
        for adept in dept_maxname:
            adept = list(adept.keys())[0]
            aname = dept_maxname[adept]
            print(adept, aname)
            print(counter + 1, adept, name_salary[aname], aname, file=out_handle)
            counter += 1
#
#
