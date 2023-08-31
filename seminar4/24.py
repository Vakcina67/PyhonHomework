list_1 = []
N = int(input('Введите количество кустов: '))
for i in range(N):
    list_1.append(int(input(f'Введите количество ягод на {i+1}-м кусте: ')))
list_2 = []
n = len(list_1)
for i in range(N-2):
    list_2.append(sum(list_1[i:i+3]))
list_2.append(list_1[0] + list_1[-2] + list_1[-1])
list_2.append(list_1[1] + list_1[0] + list_1[-1])

print(f'Максимальное число ягод: {max(list_2)}')
