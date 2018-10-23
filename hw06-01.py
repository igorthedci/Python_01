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

def dict_contains(a={}, b={}):
    """
    the function checks A-dictionary contains B-dictionary
    :param a:
    :param b:
    :return: TRUE if A contains B
    """
    result = True
    for key in b:
        if key not in a or a[key] != b[key]:
            result = False
            break
    return result


if __name__ == '__main__':

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
    hero_test = requests.get(hero_test_url).json()
    marker = dict_contains(hero_test, hero_01)
    print('Персонаж', 'создан' if marker else 'отсутствует')

# ● Проверяете, что он есть в списке персонажей по GET /roles/
    hero_test_url = url_roles
    hero_arr = requests.get(hero_test_url).json()
    marker = False
    for hero_test in hero_arr:
        marker = dict_contains(hero_test, hero_01)
        if marker:
            break
    print('Персонаж', 'создан' if marker else 'отсутствует')

# ● Изменяете этого персонажа методом PUT roles/[id]/
# hero_01 = {'name': 'Name1', 'type': 'type1', 'level': 1, 'book': 2}
    hero_test_url = url_roles+'/'+str(hero_01_id)
    hero_test = requests.put(hero_test_url).json()
    marker = dict_contains(hero_test, hero_01)
    print('Персонаж', 'создан' if marker else 'отсутствует')


    #
    #
