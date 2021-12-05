def my_func(a, b):
    if b != 0:
        c = round(a / b, 2)
    else:
        c = 'на 0 делить нельзя'
    return c
a = input('a = ')
b = input('b = ')

print(my_func(int(a), int(b)))
