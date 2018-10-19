"""
Задание 4 (на создание тестов c помощью unittest)
Создайте наборы тестов на тестирование класса ITEmployee, который вы реализовали в Задании 1
(или Employee, или Person в зависимости до куда вы дошли в выполнении Задания 1).
"""

import unittest
from hw05_01_persons import Person, Employee, ITEmployee


class PersonTests(unittest.TestCase):

    def setUp(self):
        self.somebody = Person(full_name='Roger Wilco', birth_year=1986)
        pass

    def test_01(self):
        self.assertEqual(self.somebody.full_name, 'Roger Wilco')

    def test_02(self):
        self.assertEqual(self.somebody.birth_year, 1986)

    def test_03(self):
        self.assertEqual(self.somebody.first_name(), 'Roger')

    def test_04(self):
        self.assertEqual(self.somebody.sur_name(), 'Wilco')


class EmployeeTests(unittest.TestCase):

    def setUp(self):
        self.somebody = Employee(full_name='Roger Wilco', birth_year=1986, position='Janitor', experience=12)
        pass

    def test_01(self):
        self.assertEqual(self.somebody.full_name, 'Roger Wilco')

    def test_02(self):
        self.assertEqual(self.somebody.position, 'Janitor')

    def test_03(self):
        self.assertEqual(self.somebody.exp_pos(), 'Senior Janitor')

    def test_04(self):
        self.assertEqual(self.somebody.salary, 0)

    def test_05(self):
        self.somebody.increment(10)
        self.assertEqual(self.somebody.salary, 10)

    def test_06(self):
        self.somebody.increment(-10)
        self.assertEqual(self.somebody.salary, 0)


class ITEmployeeTests(unittest.TestCase):

    def setUp(self):
        self.somebody = ITEmployee(full_name='Roger Wilco', birth_year=1986, position='Janitor', experience=12)
        pass

    def test_01(self):
        self.assertEqual(self.somebody.full_name, 'Roger Wilco')

    def test_02(self):
        self.assertEqual(self.somebody.skills, [])

    def test_03(self):
        self.somebody.add_skill()
        self.assertEqual(self.somebody.skills, [])

    def test_04(self):
        self.somebody.add_skill('smart')
        self.assertEqual(['smart'], self.somebody.skills)

    def test_05(self):
        self.somebody.add_skills()
        self.assertEqual([], self.somebody.skills)

    def test_06(self):
        self.somebody.add_skills('smart')
        self.assertEqual(['smart'], self.somebody.skills)

    def test_07(self):
        self.somebody.add_skills('smart', 'cool')
        self.assertEqual(['smart', 'cool'], self.somebody.skills)

#
if __name__ == '__main__':
    unittest.main()
#