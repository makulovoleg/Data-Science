
def simple_calc(hours_worked, sum_pay, awards):
    return (hours_worked * sum_pay) + awards


hours_worked = float(input('Введите количество отработанных часов : '))
sum_pay = float(input('Введите суммы оплаты труда за 1 час : '))
awards = float(input('Укажите размер премии - '))
print(f'Размер заработной платы составил: {simple_calc(hours_worked, sum_pay, awards) }')
