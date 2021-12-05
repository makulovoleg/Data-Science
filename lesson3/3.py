def my_func(arg1, arg2, arg3):
    print(f'сумма наибольших двух аргументов: {arg1+arg2+arg3- min([arg1, arg2, arg3])}')

my_func(
    int(input('Аргумент1 ')),
    int(input('Аргумент2 ')),
    int(input('Аргумент3 '))
)