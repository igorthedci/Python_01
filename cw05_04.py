from cw05_03 import Person

class EmployeeInfopulse(Person):

    """  class description """
    def income(self):
        return 'Not defined'

    def year_income(self, months):
        return self.salary * months

    # def __init__(self, position=None, salary=0, *args, **kwargs):
    def __init__(self, name='', surname='', age=0, position=None, salary=0):
        # Person.__init__(self, *args, **kwargs)
        # Person.__init__(self, name, surname, age)
        # self.name = name
        # self.surname = surname
        # self.age = age
        super().__init__(name, surname, age) # !!!!!  SELF is absent
        self.position = position
        self.salary = salary
        self.skills = []

    def add_skill(self, new_skill):
        self.skills.append(new_skill)

if __name__ == '__main__':
    e1 = EmployeeInfopulse(name='Ol')
    print(str(e1))
    print(e1)
    print(e1.income())
