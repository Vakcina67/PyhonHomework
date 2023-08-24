import math
s = int(input('Введите сумму чисел S: '))
p = int(input('Введите произведение чисел P: '))

x = (s + int(math.sqrt(s ** 2 - 4 * p))) // 2
y = (s - int(math.sqrt(s ** 2 - 4 * p))) // 2

if x | y > 1000:
    print('Вы ввели некорректную сумму или произведение!')
else:
    print(f'Числа X и Y: {x} и {y}')
