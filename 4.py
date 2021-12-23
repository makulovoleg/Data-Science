file = open('task4.txt', 'r', encoding = 'utf_8')
stroki = file.readlines()
rus = {
    'One': 'один',
    'Two': 'два',
    'Three': 'три',
    'Four': 'четыре'
}
new_spisok = []
for i in stroki:
    i = i.split(' ', 1)
    new_spisok.append(rus[i[0]] + ' ' + i[1])

with open('task4_new.txt', 'w') as new_file:
    new_file.writelines(new_spisok)


