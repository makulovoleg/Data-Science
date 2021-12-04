month = input('Введите номер месяца: ')

z = 'Зима'
v = 'Весна'
l = 'Лето'
o = 'Осень'

sizon = {'1': z, '2': z, '3': v, '4': v, '5': v, '6': l, '7': l, '8':l, '9':o, '10': o, '11': o, '12': o}
print(sizon[month])

sizon1 = [z, z, v, v, v, l, l, l, o, o, o, z]
print(sizon1[int(month) - 1])
