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
    arr_person = []  # item = { id: Имя_Фамилия, dept: Отдел, salary: Зарплата }
    with open(in_file, encoding='utf-8') as in_handle:
        aline = in_handle.readline().strip()
        titles = aline.split(' ')
        key_id = titles[1] + '_' + titles[0]
        key_dept = titles[2]
        key_salary = titles[3]
        print(key_id, key_dept, key_salary)
        for aline in in_handle:
            aline = aline.strip().split(' ')
            arr_person.append( { key_id: aline[1]+'_'+aline[0], key_dept: aline[2], key_salary: aline[3] } )
#
# 1 Посчитайте сколько отделов на фирме
    arr_dept = []  # item = [ Отдел ]
    for aperson in arr_person:
        adept = aperson[key_dept]
        if adept not in arr_dept:
            arr_dept.append(adept)
    pass
#
    with open(out_file, 'a', encoding='utf-8') as out_handle:
        print("Количество отделов :", len(arr_dept), file=out_handle)
        counter = 0
        for adept in arr_dept:
            print(counter+1, arr_dept[counter], file=out_handle)
            counter += 1
#
# 2 Определите максимальную зарплату
    salary_max = 0
    for aperson in arr_person:
        if salary_max < int(aperson[key_salary]):
            salary_max = int(aperson[key_salary])
#
    with open(out_file, 'a', encoding='utf-8') as out_handle:
        print("\nМаксимальная зарплата на фирме :", salary_max, file=out_handle)
#
# 3 Определите максимальную зарплату в каждом отделе
# 4 Выведите «Отдел Макс_Зарплата  Фамилия_человека_с_такой_зарплатой» в новый файл
# (составляется список {отдел : сотрудник_с максимальной_зарплатой}
    salary_max = []  # item = { key: dept, value: Имя_Фамилия }
    for aperson in arr_person:
        if aperson[key_dept] not in salary_max:
            salary_max.append( { aperson[key_dept]: aperson[key_id]} )
        else:
            adept = aperson[key_dept]
            aname = salary_max[adept]
            if aperson[key_salary] > arr_person[aname][key_salary]:
                salary_max[adept] = aname
#
    with open(out_file, 'a', encoding='utf-8') as out_handle:
        print("\nМаксимальная зарплат по отделам", file=out_handle)
        counter = 0
        for adept in salary_max:
            print(adept)
            aname = str(adept.values())
            print(counter + 1, adept.keys(), arr_person[aname].get(key_salary), aname, file=out_handle)
            counter += 1
#
#
