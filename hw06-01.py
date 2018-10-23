import requests
"""
Тестовое приложение с REST API ​ ttp://pulse-rest-testing.herokuapp.com/
Создаём один скрипт:
● Создаёт персонажа POST /roles/, вы запоминаете его id.
● Проверяете, что он создался и доступен по ссылке GET /roles/[id]
● Проверяете, что он есть в списке пользователей по GET /roles/
● Изменяете этого пользователя методом PUT roles/[id]/
● Проверяете, что он изменился и доступен по ссылке /roles/[id]
● Проверяете, что он есть в списке пользователей по GET /roles/ с новой инфой
● Удаляете этого пользователя методом DELETE roles/[id]
● Второй скрипт: тоже самое с книгами

   Попробуйте воспользоваться http.client вместо requests. Ощутите разницу
"""
url_books = 'http://pulse-rest-testing.herokuapp.com/books'
url_roles = 'http://pulse-rest-testing.herokuapp.com/roles'

# ● Создаёт персонажа POST /roles/, вы запоминаете его id.
hero_01 = {'name': 'Name1', 'type': 'type1', 'level': 1, 'book': 2}
# r = requests.post(url_roles, data=hero_01)
# print(r.status_code)
# r_dict = r.json()
# print(r_dict)
# hero_01_id = r.json()['id']
hero_01_id = 12
# print(hero_01_id)

# ● Проверяете, что он создался и доступен по ссылке GET /roles/[id]
hero_test_url = url_roles+'/'+str(hero_01_id)
# print(hero_test_url)
hero_test = requests.get(hero_test_url).json()
marker = True
for key in hero_01:
    if key not in hero_test or hero_01[key] != hero_test[key]:
        marker = False
        break
print(marker)

# r2 = requests.delete(url_books+'/'+str(r_dict['id']))
# print(r2.status_code)
# print(r2.url)
# print(r2.json())
# r2_dict = r2.json()
# print(r2_dict)


if __name__ == '__main__':
    pass
#
#
