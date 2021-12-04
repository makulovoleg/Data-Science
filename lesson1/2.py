sec = int(input('Введите время в секундах: '))

sec = sec % 86400
hour = sec // 3600
sec = sec % 3600
min = sec // 60
sec = sec % 60

print(f'Часы {hour} Минуты {min} Секунды {sec}')


