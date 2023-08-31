n = int(input('Введите количество элементов первого множества: '))
m = int(input('Введите количество элементов второго множества: '))
list_1 = []
list_2 = []
for i in range(n):
    list_1.append(int(input(f'Введите {i+1}-й элемент первого множества: ')))
for i in range(m):
    list_2.append(int(input(f'Введите {i+1}-й элемент второго множества: ')))

set_1 = set(list_1)
set_2 = set(list_2)

set_final = set_1.intersection(set_2)

list_final = list(set_final)
list_final.sort()
print(list_final)
