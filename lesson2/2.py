spisok = input('Список: ')
spisok = spisok.split()
i = 0
while i < len(spisok) - 1:
    spisok[i], spisok[i + 1] = spisok[i + 1], spisok[i]
    i = i + 2
print(spisok)
