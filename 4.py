c = int(input('Введите число: '))
a = c % 10
b = a // 10

while c > 0:
    if c % 10 > a:
        a = c % 10
    c = c // 10
print(a)






