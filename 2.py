file = open('task2.txt', 'r', encoding = 'utf_8')
stroki = file.readlines()
print(f'количества строк {len(stroki)}')
a = 1
for i in stroki:
    slova = i.split()
    print(f'количества слов в {a} строке: {len(slova)}')
    a+=1
file.close()
