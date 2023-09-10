from random import randint


def range_func(a, b, start_list):
    new_list = []
    for i in range(len(start_list)):
        if a <= start_list[i] and b >= start_list[i]:
            new_list.append(i)
    return new_list


start_len = int(input('Введите число элементов начального списка: '))
min_num = int(input('Введите минимальное число диапазона: '))
max_num = int(input('Введите максимальное число диапазона: '))
my_list = [randint(-1000, 1000) for i in range(start_len)]

print('Элементы списка в диапазоне: {}'.format(
    range_func(min_num, max_num, my_list)))
