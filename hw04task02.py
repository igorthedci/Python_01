import math
import random

# Задание 2
# Пишем функцию, которая выводит второе по возрастанию значение из переданных аргументов.
# Учитываем, что может быть повторяющиеся значения аргументов.


def second_max(*nums):
    nums = list(nums)
    nums.sort()
    return nums[-2]


nums = [math.floor(random.random() * 100.) for i in range(20)]
print(nums)
second = second_max(*nums)
print(nums)
print(second)
