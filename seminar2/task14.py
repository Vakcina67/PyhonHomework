n = int(input('Введите натуральное число N: '))
k = 1
while 2 ** k < n:
    print(2 ** k)
    k += 1
