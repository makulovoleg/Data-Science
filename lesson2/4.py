stroka = input('Ведите строку: ')

stroka = stroka.split()
i = 1
for slovo in stroka:
    print(f'{i} {slovo[:10]}')
    i = i+1