
# Задание 3
#  C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use sorted() function and a custom key= function to extract the last element form each tuple.


def take_last(elem):
    return elem[-1]


def sort_last(tuples):
    # +++your code here+++
    sorted_tuples = sorted(tuples, key=take_last)
    return sorted_tuples


def random_tuple(max_l = 2, max_h = 10):
    max_l = 1 + math.floor(random.random() * max_l)
#    max_h = 1 + math.floor(random.random() * max_h)
    atuple = [math.floor(random.random() * max_h) for x in range(max_l)]  # !!!! its LIST, not TUPLE
    return atuple


if __name__ == '__main__':
#
    array_length = 10
    random_list = [random_tuple(3) for x in range(array_length)]
    sorted_list = sort_last(random_list)
    print('{:<20}{:<20}'.format('Random list', 'Sorted list'))
    for i in range(array_length):
        str1 = '[' + ' ,'.join(str(x) for x in random_list[i]) + ']'
        str2 = '[' + ' ,'.join(str(x) for x in sorted_list[i]) + ']'
        print('{:<20}{:<20}'.format(str1, str2))

