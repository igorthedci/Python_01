
class Person:

    def __init__(self, name='', surname='', age=0):
        self.name = name
        self.surname = surname
        self.age = age

    def full_name(self):
        print(self.name, self.surname)
        return self.name + ' ' + self.surname

    def get_older(self, years):
        ''' увеличивает возраст на years лет '''
        self.age += years

    def __str__(self):
        ''' преобразование объекта в строку '''
        return "<Person object: {} {}>".format(self.name, self.surname)

if __name__ == '__main__':
    neo = Person('Neo', 'Anderson', 0)
    neo.full_name()
    print(neo.full_name())
    neo.get_older(10)
    print(neo.age)
    print(str(neo))
#