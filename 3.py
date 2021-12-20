file = open('oklady.txt', 'r', encoding = 'utf_8')
spisok = file.read().split('\n')
fio = []
oklad = []
for i in spisok:
    i = i.split()
    oklad.append(i[1])
    if int(i[1]) < 20000:
        fio.append(i[0])
print(f'оклад меньше 20 тыс руб: {fio}\nсредний оклад: {sum(map(int, oklad))/len(oklad)}')
