from math import factorial

def fact(n):
    for i in range(n + 1):

        yield factorial(i)

n = int(input('введите число '))
for i in fact(n):

    print(i)
