a = int(input('Введите выручку: '))
b = int(input('Введите издержеки: '))
if a - b > 0:
    print('Прибыль — выручка больше издержек')

    print(f'Рентабельность: {(a / b):.2f}')
    c = int(input('Введите численность сотрудников фирмы: '))
    print(f'прибыль фирмы в расчете на одного сотрудника {(a / c):.2f}')
else:
    print('Убыток — издержки больше выручки')
