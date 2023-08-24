monets = input('Введите выпавшие стороны монеток (р или г) через пробел: ').split()
n = len(monets)
i = 0
j = 0

for k in range(n):
    if monets[k] == 'р':
        i += 1
    else:
        j += 1
if i < j:
    print(i)
else:
    print(j)