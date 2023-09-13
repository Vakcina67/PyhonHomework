my_data = input('Введите фразы через пробел: ').lower().split()
vowels = set('аоуэыиеёюя')


def vowel_count(str):
    return len([v for v in str if v in vowels])


count_set = set(map(vowel_count, my_data))
if len(count_set) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')
