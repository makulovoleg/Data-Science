from itertools import count, cycle

print('итератор, генерирующий целые числа, начиная с указанного')
for i in count(3):
    print(i, end=' ')
    if i == 10:
        break

print('\nитератор, повторяющий элементы некоторого списка, определенного заранее')
list = [5, 3, 3, 1, 0, 4, 2, 4, 7, 3]
a = 0
for b in cycle(list):
    print(b, end=' ')
    a = a + 1
    if a == 100:
        break
