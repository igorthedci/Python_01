import requests
"""
Тестовое приложение с REST API ​ ttp://pulse-rest-testing.herokuapp.com/
Создаём один скрипт:
1● Создаёт персонажа POST /roles/, вы запоминаете его id.
2● Проверяете, что он создался и доступен по ссылке GET /roles/[id]
3● Проверяете, что он есть в списке персонажа по GET /roles/
4● Изменяете этого персонажа методом PUT roles/[id]/
5● Проверяете, что он изменился и доступен по ссылке /roles/[id]
6● Проверяете, что он есть в списке персонажа по GET /roles/ с новой инфой
7● Удаляете этого персонажа методом DELETE roles/[id]
8● Второй скрипт: тоже самое с книгами

   Попробуйте воспользоваться http.client вместо requests. Ощутите разницу
"""

def dict_contains(a={}, b={}):
    """
    :param a: dictionary
    :param b: dictionary
    :return: TRUE if A-dict contains B-dict
    """
    result = True
    for key in hero_01:
        if key not in hero_test or hero_01[key] != hero_test[key]:
            marker = False
            break
    return result

if __name__ == '__main__':

    url_books = 'http://pulse-rest-testing.herokuapp.com/books'
    url_roles = 'http://pulse-rest-testing.herokuapp.com/roles'

# 1● Создаёт персонажа POST /roles/, вы запоминаете его id.
    hero_01 = {'name': 'Name1', 'type': 'type1', 'level': 1, 'book': 2}
    hero_01_id = requests.post(url_roles, hero_01).json()['id']
    print('Создан персонаж с номером', hero_01_id)
#    hero_01_id = 12

# 2● Проверяете, что он создался и доступен по ссылке GET /roles/[id]
    hero_test_url = url_roles+'/'+str(hero_01_id)
    hero_test = requests.get(hero_test_url).json()
    marker = dict_contains(hero_test, hero_01)
    print('Персонаж', 'существует' if marker else 'отсутствует.')

# 3● Проверяете, что он есть в списке персонажа по GET /roles/
    hero_list = requests.get(url_roles).json()
    marker = False
    for hero_test in hero_list:
        marker = dict_contains(hero_test, hero_01)
        if marker: break
    print('Персонаж', 'существует' if marker else 'отсутствует.')

# 4● Изменяете этого персонажа методом PUT roles/[id]/
    hero_01 = {'name': 'Name1new', 'type': 'type1new', 'level': 2, 'book': 2}
    hero_test_url = url_roles+'/'+str(hero_01_id)
    hero_test = requests.put(hero_test_url, hero_01).json()
    marker = dict_contains(hero_test, hero_01)
    print('Персонаж', 'обновлен' if marker else 'остался прежним.')

# 5● Проверяете, что он изменился и доступен по ссылке /roles/[id]
    hero_test_url = url_roles+'/'+str(hero_01_id)
    hero_test = requests.get(hero_test_url).json()
    marker = dict_contains(hero_test, hero_01)
    print('Изменение', 'правильно.' if marker else 'отсутствует.')

# 6● Проверяете, что он есть в списке персонажа по GET /roles/ с новой инфой
    hero_list = requests.get(url_roles).json()
    marker = False
    for hero_test in hero_list:
        marker = dict_contains(hero_test, hero_01)
        if marker: break
    print('Изменение', 'правильно.' if marker else 'отсутствует.')

# 7● Удаляете этого персонажа методом DELETE roles/[id]
    hero_test_url = url_roles+'/'+str(hero_01_id)
    hero_test = requests.delete(hero_test_url)
    print(hero_test.status_code)
    print('Изменение', 'правильно.' if marker else 'отсутствует.')
