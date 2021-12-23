from random import randint
file = open('task5.txt', 'w', encoding ='utf_8')
for i in range(100):
    file.writelines(str(f'{randint(0,100)} '))
file.close()

file = open('task5.txt', 'r', encoding ='utf_8')
stroka = file.readline().split()
a = 0
for i in stroka:
    a = a + int(i)
print(a)



