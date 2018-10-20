import datetime


class Person:
    """
    CLASS Person (два свойства:
    1) full_name пусть будет свойством, а не функцией, а свойств name и surname нет
    (одно поле, тип строка и состоит из двух слов «имя фамилия»),
    2) год рождения).
    """

    def __init__(self, full_name=None, birth_year=None):
        """
    ** (только для продвинутых) в конструкторе проверить, что в full_name
    передаётся строка, состоящая из двух слов, если нет, вызывайте исключение
    ** (только для продвинутых) в конструкторе проверить, что в год рождения
    меньше 2018, но больше 1900, если нет вызывайте исключение
        """
        if len(full_name.split(' ')) != 2:
            raise ValueError('Incorrect full_name. Required format: two words.')
        self.full_name = full_name
        current_year = datetime.datetime.now().year
        if not birth_year:
            self.birth_year = birth_year
        elif 1900 <= birth_year <= current_year:
            self.birth_year = birth_year
        else:
            raise ValueError('Incorrect birth_year. Required value between 1900 and ' + str(current_year))

    def first_name(self):
        # print(self)
        return self.full_name.split(' ')[0]

    def sur_name(self):
        # print(self)
        return self.full_name.split(' ')[1]

    def age_in(self, year = 0):
        """
        вычисляет сколько лет есть/исполнится в году, который передаётся параметром
        """
        now = datetime.datetime.now()
        if not year:
            return now.year - self.birth_year
        if year < self.birth_year:
            return 0
        else:
            return year - self.birth_year

    def __str__(self):
        """ преобразование объекта в строку """
        return "<PERSON object:: full_name:{}, birth_year:{}>".format(self.full_name, self.birth_year)


class Employee(Person):
    """
    Employee (наследуемся от Person)
    (добавляются свойства:
    1) должность, 2) опыт работы, 3) зарплата)
    """
    def __init__(self, full_name='', birth_year=0, position='', salary=0, experience=0):
        super().__init__(full_name=full_name, birth_year=birth_year)
        self.position = position
        self.salary = salary
        self.experience = experience

    def increment(self, value):
        self.salary += value
        if self.salary < 0:
            self.salary = 0

    def exp_pos(self):
        prefix = 'Senior' if self.experience >= 6 \
            else ('Middle' if self.experience >= 3 else 'Junior')
        return prefix + ' ' + self.position

    def __str__(self):
        """ преобразование объекта в строку """
        return "<EMPLOYEE object:: full_name:{} birth_year:{}\n " \
               "position:{} salary:{} experince:{}>"\
            .format(self.full_name, self.birth_year,
                    self.exp_pos(), self.salary, self.experience)


class ITEmployee(Employee):
    """
    ITEmployee (наследуемся от Employee)
    1. Реализовать метод добавления одного навыка в новое свойство skills (список) новым
    методом add_skill (см. презентацию).
    2. * Реализовать метод добавления нескольких навыков в новое свойство skills (список)
    новым методом add_skills.
    Тут можно выбрать разные подходы: или аргумент один и он список навыков, которым вы
    расширяете список-свойство skill, или вы принимаете неопределённое количество
    аргументов, и все их добавляете в список-свойство skill
    """
    def __init__(self, full_name='', birth_year=0, position='', salary=0, experience=0, *skills):
        super().__init__(full_name=full_name, birth_year=birth_year,
                         position=position, salary=salary, experience=experience)
        self.skills = list(*skills)

    def add_skill(self, new_skill=''):
        if not new_skill:
            return
        try:
            if self.skills.index(new_skill) >= 0:
                return
        except:
            self.skills.append(new_skill)
            return
            # self.skills = []

    def add_skills(self, *new_skills):
        for item in new_skills:
            self.skills.append(item)

    def __str__(self):
        """ преобразование объекта в строку """
        return "<ITEMPLOYEE object:: full_name:{} birth_year:{}\n" \
               "position:{} salary:{} experince:{}\n" \
               "skills:{}>"\
            .format(self.full_name, self.birth_year,
                    self.exp_pos(), self.salary, self.experience, self.skills)


if __name__ == '__main__':
    neo = Person(full_name='Neo Anderson', birth_year=1999)
    print(neo.first_name())
    print(neo.sur_name())
    neo.age_in()
    print(neo.birth_year)
    print(str(neo))
#
    roger = Employee(full_name='Roger Wilco', birth_year=1986, position='Janitor', experience=12)
    print(str(roger))
#
    neo = ITEmployee(full_name='Neo Anderson', birth_year=1999, position='Chosen', experience=1)
    neo.add_skills('cool', 'smart')
    print(str(neo))
#